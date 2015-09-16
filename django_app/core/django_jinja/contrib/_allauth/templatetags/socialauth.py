# coding: utf-8
from django_jinja import library
from allauth.socialaccount import providers
from allauth.utils import get_request_param


@library.global_function
def provider_login_url(request, provider_id, **kwargs):
    """
    See allauth/socialaccount/templatetags/socialaccount.py
    """
    provider = providers.registry.by_id(provider_id)
    auth_params = kwargs.get('auth_params', None)
    scope = kwargs.get('scope', None)
    process = kwargs.get('process', None)
    if scope is '':
        del kwargs['scope']
    if auth_params is '':
        del kwargs['auth_params']
    if 'next' not in kwargs:
        next = get_request_param(request, 'next')
        if next:
            kwargs['next'] = next
        elif process == 'redirect':
            kwargs['next'] = request.get_full_path()
    else:
        if not kwargs['next']:
            del kwargs['next']
    # get the login url and append kwargs as url parameters
    return provider.get_login_url(request, **kwargs)


@library.global_function
def providers_media_js(request):
    """
    See allauth/socialaccount/templatetags/socialaccount.py
    """
    return '\n'.join([p.media_js(request) for p in providers.registry.get_list()])


@library.global_function
def get_providers():
    """
    See allauth/socialaccount/templatetags/socialaccount.py
    """
    return providers.registry.get_list()
