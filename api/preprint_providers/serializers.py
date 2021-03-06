from rest_framework import serializers as ser

from api.base.utils import absolute_reverse
from api.base.serializers import JSONAPISerializer, LinksField, RelationshipField


class PreprintProviderSerializer(JSONAPISerializer):

    filterable_fields = frozenset([
        'name',
        'description',
        'id',
        'domain',
        'domain_redirect_enabled'
    ])

    name = ser.CharField(required=True)
    description = ser.CharField(required=False)
    id = ser.CharField(max_length=200, source='_id')
    advisory_board = ser.CharField(required=False, allow_null=True)
    email_contact = ser.CharField(required=False, allow_null=True)
    email_support = ser.CharField(required=False, allow_null=True)
    example = ser.CharField(required=False, allow_null=True)
    domain = ser.CharField(required=False, allow_null=False)
    domain_redirect_enabled = ser.BooleanField(required=True)
    social_twitter = ser.CharField(required=False, allow_null=True)
    social_facebook = ser.CharField(required=False, allow_null=True)
    social_instagram = ser.CharField(required=False, allow_null=True)
    header_text = ser.CharField(required=False, allow_null=True)
    subjects_acceptable = ser.JSONField(required=False, allow_null=True)
    logo_path = ser.CharField(read_only=True)
    banner_path = ser.CharField(read_only=True)
    share_source = ser.CharField(read_only=True)

    preprints = RelationshipField(
        related_view='preprint_providers:preprints-list',
        related_view_kwargs={'provider_id': '<_id>'}
    )

    taxonomies = RelationshipField(
        related_view='preprint_providers:taxonomy-list',
        related_view_kwargs={'provider_id': '<_id>'}
    )

    licenses_acceptable = RelationshipField(
        related_view='preprint_providers:license-list',
        related_view_kwargs={'provider_id': '<_id>'}
    )

    links = LinksField({
        'self': 'get_absolute_url',
        'preprints': 'get_preprints_url',
        'external_url': 'get_external_url'
    })

    class Meta:
        type_ = 'preprint_providers'

    def get_absolute_url(self, obj):
        return obj.absolute_api_v2_url

    def get_preprints_url(self, obj):
        return absolute_reverse('preprint_providers:preprints-list', kwargs={
            'provider_id': obj._id,
            'version': self.context['request'].parser_context['kwargs']['version']
        })

    def get_external_url(self, obj):
        return obj.external_url
