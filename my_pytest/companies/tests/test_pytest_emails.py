import json
from unittest.mock import patch

from django.core import mail
from django.test import Client

import pytest


def test_send_email_should_succeed(mailoutbox, settings) -> None:
    settings.EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
    assert len(mailoutbox) == 0

    # Send message
    mail.send_mail(
        subject='Test subject',
        message='Test message',
        from_email='test@test.kz',
        recipient_list=['test1@test.kz'],
        fail_silently=False,
    )

    # Test that one message has been sent
    assert len(mailoutbox) == 1

    # Verify that the subject of the first message is correct
    assert mailoutbox[0].subject == 'Test subject'


def test_send_email_without_arguments_should_send_empty_email(client) -> None:
    with patch('companies.views.send_mail') as mocked_send_mail_function:
        response = client.post(path='/send-email')
        response_content = json.loads(response.content)
        assert response.status_code == 200
        assert response_content['status'] == 'success'
        assert response_content['info'] == 'email sent successfully'
        mocked_send_mail_function.assert_called_with(
            subject=None,
            message=None,
            from_email='mila-iris@mila-iris.kz',
            recipient_list=['mila-iris@mila-iris.kz'],
        )


def test_send_email_with_get_verb_should_fail(client) -> None:
    response = client.get(path='/send-email')
    assert response.status_code == 405
    assert json.loads(response.content) == {'detail': 'Method "GET" not allowed.'}
