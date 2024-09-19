# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin



class Beneficiaries(models.Model):
    oid = models.UUIDField(primary_key=True)
    name = models.TextField(unique=True)
    code = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    info = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beneficiaries'


class Companies(models.Model):
    oid = models.UUIDField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    slug = models.TextField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    customer_oid = models.TextField(blank=True, null=True)
    invoicing_email = models.TextField(blank=True, null=True)
    fiscal_address = models.TextField(blank=True, null=True)
    postal_code = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    has_accepted_contract = models.BooleanField()
    has_accepted_terms_of_service = models.BooleanField()
    has_accepted_privacy_policy = models.BooleanField()
    owner_oid = models.ForeignKey('Users', models.DO_NOTHING, db_column='owner_oid', blank=True, null=True)
    subscription_oid = models.TextField(blank=True, null=True)
    plan = models.TextField(blank=True, null=True)
    vat = models.TextField(unique=True, blank=True, null=True)
    cif = models.TextField(unique=True, blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    apikey = models.TextField(blank=True, null=True)
    delete_at_period_end = models.BooleanField(blank=True, null=True)
    deleted = models.BooleanField(blank=True, null=True)
    webhook = models.TextField(blank=True, null=True)
    beneficiary_oid = models.ForeignKey(Beneficiaries, models.DO_NOTHING, db_column='beneficiary_oid', blank=True, null=True)
    language = models.TextField()  # This field type is a guess.
    push_api_key = models.JSONField(blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)
    schedule_oid = models.ForeignKey('TrackingSchedules', models.DO_NOTHING, db_column='schedule_oid', blank=True, null=True)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'


class CompaniesPois(models.Model):
    oid = models.UUIDField(primary_key=True)
    company_oid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_oid')
    poi_oid = models.ForeignKey('Pois', models.DO_NOTHING, db_column='poi_oid')

    class Meta:
        managed = False
        db_table = 'companies_pois'
        unique_together = (('company_oid', 'poi_oid'),)


class CompanyCreditsUsage(models.Model):
    oid = models.UUIDField(primary_key=True)
    company_oid = models.OneToOneField(Companies, models.DO_NOTHING, db_column='company_oid')
    start_billing = models.DateTimeField(blank=True, null=True)
    end_billing = models.DateTimeField(blank=True, null=True)
    initial_credits = models.IntegerField()
    dashboard_credits = models.IntegerField()
    api_credits = models.IntegerField()
    link_credits = models.IntegerField()
    request_oid = models.TextField(blank=True, null=True)  # This field type is a guess.
    remaining_credits = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_credits_usage'


class CompanyCreditsUsageHistoric(models.Model):
    oid = models.UUIDField(primary_key=True)
    company_oid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_oid')
    start_billing = models.DateTimeField()
    end_billing = models.DateTimeField()
    initial_credits = models.IntegerField()
    dashboard_credits = models.IntegerField()
    api_credits = models.IntegerField()
    link_credits = models.IntegerField()
    remaining_credits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'company_credits_usage_historic'


class Credentials(models.Model):
    oid = models.UUIDField(primary_key=True)
    data = models.TextField()
    provider = models.TextField()
    status = models.BooleanField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    auto_import = models.BooleanField()
    company_oid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_oid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credentials'


class CreditMovements(models.Model):
    oid = models.UUIDField(primary_key=True)
    company_oid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_oid')
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    amount = models.IntegerField()
    data = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'credit_movements'


class CreditMovementsHistoric(models.Model):
    oid = models.UUIDField(primary_key=True)
    company_oid = models.UUIDField()
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    amount = models.IntegerField()
    data = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'credit_movements_historic'
        unique_together = (('oid', 'date'),)



class Drivers(models.Model):
    oid = models.UUIDField(primary_key=True)
    fullname = models.TextField()
    email = models.TextField()
    password = models.TextField()
    validated = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    recover_password_token = models.TextField(blank=True, null=True)
    recover_password_token_expiration_date = models.DateTimeField(blank=True, null=True)
    has_accepted_terms_and_conditions = models.BooleanField()
    has_accepted_marketing_contact = models.BooleanField()
    tracker_id = models.TextField()
    last_access_timestamp = models.DateTimeField(blank=True, null=True)
    company_oid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_oid')
    status = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'drivers'
        unique_together = (('email', 'tracker_id'),)


class EndpointCredits(models.Model):
    endpoint = models.CharField(max_length=255)
    credits = models.IntegerField()
    category = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'endpoint_credits'


class Events(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class FeatureRoles(models.Model):
    role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)
    feature = models.ForeignKey('Features', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    permissions = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'feature_roles'
        unique_together = (('role', 'feature', 'product'),)


class Features(models.Model):
    feature_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'features'


class FuelTypes(models.Model):
    oid = models.UUIDField(primary_key=True)
    name = models.TextField(unique=True)
    info = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuel_types'


class Groups(models.Model):
    oid = models.UUIDField(primary_key=True)
    name = models.TextField()
    slug = models.TextField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    user_oid = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_oid', blank=True, null=True)
    webhook = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    subscribed_pois = models.TextField(blank=True, null=True)  # This field type is a guess.
    company_oid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_oid', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    schedule_oid = models.ForeignKey('TrackingSchedules', models.DO_NOTHING, db_column='schedule_oid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class GroupsTrackers(models.Model):
    oid = models.UUIDField(primary_key=True)
    group_oid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='group_oid')
    tracker_oid = models.ForeignKey('Trackers', models.DO_NOTHING, db_column='tracker_oid')

    class Meta:
        managed = False
        db_table = 'groups_trackers'
        unique_together = (('group_oid', 'tracker_oid'),)


class LastTrackerProperties(models.Model):
    tracker_oid = models.UUIDField()
    key = models.IntegerField()
    value = models.FloatField()
    ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'last_tracker_properties'


class LinkEvents(models.Model):
    oid = models.UUIDField(primary_key=True)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    computed_operations = models.IntegerField(blank=True, null=True)
    billed_on = models.DateTimeField(blank=True, null=True)
    link_type = models.ForeignKey('LinkTypes', models.DO_NOTHING, db_column='link_type')
    tracker_oid = models.ForeignKey('Trackers', models.DO_NOTHING, db_column='tracker_oid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_events'


class LinkTypes(models.Model):
    link_type = models.CharField(max_length=255)
    data = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'link_types'


class Metrics(models.Model):
    id = models.UUIDField(primary_key=True)
    ts = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    caller = models.CharField(max_length=255, blank=True, null=True)
    context = models.TextField(blank=True, null=True)  # This field type is a guess.
    answer = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'metrics'


class Motorizations(models.Model):
    oid = models.UUIDField(primary_key=True)
    name = models.TextField(unique=True)
    electric = models.BooleanField(blank=True, null=True)
    combustion = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    info = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'motorizations'


class NotificationInbox(models.Model):
    oid = models.UUIDField(primary_key=True)
    user_oid = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_oid', blank=True, null=True)
    event_type = models.TextField()
    group_oid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='group_oid', blank=True, null=True)
    tracker_oid = models.ForeignKey('Trackers', models.DO_NOTHING, db_column='tracker_oid', blank=True, null=True)
    notification_oid = models.ForeignKey('NotificationRules', models.DO_NOTHING, db_column='notification_oid')
    created_at = models.DateTimeField()
    is_favorite = models.BooleanField(blank=True, null=True)
    is_read = models.BooleanField(blank=True, null=True)
    info = models.JSONField()
    trash = models.BooleanField(blank=True, null=True)
    company_oid = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_inbox'


class NotificationInboxStatuses(models.Model):
    oid = models.UUIDField()
    notification_inbox_oid = models.ForeignKey(NotificationInbox, models.DO_NOTHING, db_column='notification_inbox_oid', blank=True, null=True)
    user_oid = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_oid', blank=True, null=True)
    favorite = models.BooleanField()
    read = models.BooleanField()
    trash = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'notification_inbox_statuses'


class NotificationRules(models.Model):
    oid = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    group_oid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='group_oid', blank=True, null=True)
    tracker_oid = models.ForeignKey('Trackers', models.DO_NOTHING, db_column='tracker_oid', blank=True, null=True)
    poi_oid = models.ForeignKey('Pois', models.DO_NOTHING, db_column='poi_oid', blank=True, null=True)
    car = models.BooleanField(blank=True, null=True)
    bike = models.BooleanField(blank=True, null=True)
    kickscooter = models.BooleanField(blank=True, null=True)
    van = models.BooleanField(blank=True, null=True)
    motorbike = models.BooleanField(blank=True, null=True)
    inside_poi = models.BooleanField(blank=True, null=True)
    outside_poi = models.BooleanField(blank=True, null=True)
    notify_by_email = models.BooleanField(blank=True, null=True)
    notify_by_webhook = models.BooleanField(blank=True, null=True)
    user_oid = models.UUIDField(blank=True, null=True)
    trips_max_kms_in_total = models.IntegerField(blank=True, null=True)
    trips_max_kms_per_day = models.IntegerField(blank=True, null=True)
    trips_max_kms_per_month = models.IntegerField(blank=True, null=True)
    trips_max_kms_per_week = models.IntegerField(blank=True, null=True)
    close_to_poi = models.BooleanField(blank=True, null=True)
    min_distance_to_poi = models.IntegerField(blank=True, null=True)
    deleted = models.BooleanField()
    enable_rule_at = models.DateTimeField()
    disable_rule_at = models.DateTimeField()
    company_oid = models.UUIDField(blank=True, null=True)
    max_time_at_poi = models.IntegerField(blank=True, null=True)
    odometer_maintenance = models.IntegerField(blank=True, null=True)
    movement_time_slot_start = models.TextField(blank=True, null=True)
    movement_time_slot_end = models.TextField(blank=True, null=True)
    days_of_the_week = models.TextField(blank=True, null=True)  # This field type is a guess.
    report_7days_inactive = models.BooleanField(blank=True, null=True)
    rule_email = models.TextField(blank=True, null=True)
    push_park = models.BooleanField(blank=True, null=True)
    truck = models.BooleanField(blank=True, null=True)
    helicopter = models.BooleanField(blank=True, null=True)
    drone = models.BooleanField(blank=True, null=True)
    airplane = models.BooleanField(blank=True, null=True)
    boat = models.BooleanField(blank=True, null=True)
    bus = models.BooleanField(blank=True, null=True)
    ambulance = models.BooleanField(blank=True, null=True)
    taxi = models.BooleanField(blank=True, null=True)
    tractor = models.BooleanField(blank=True, null=True)
    caravan = models.BooleanField(blank=True, null=True)
    enable = models.BooleanField(blank=True, null=True)
    link_type = models.ForeignKey(LinkTypes, models.DO_NOTHING, db_column='link_type', blank=True, null=True)
    webhook = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_rules'


class NotificationsThrottling(models.Model):
    oid = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    tracker_oid = models.ForeignKey('Trackers', models.DO_NOTHING, db_column='tracker_oid', blank=True, null=True)
    notification_rule_oid = models.ForeignKey(NotificationRules, models.DO_NOTHING, db_column='notification_rule_oid', blank=True, null=True)
    notified = models.IntegerField(blank=True, null=True)
    telemetric_oid = models.UUIDField(blank=True, null=True)
    tracker_property_oid = models.UUIDField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications_throttling'


class Packages(models.Model):
    oid = models.UUIDField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    provider_oid = models.ForeignKey('Providers', models.DO_NOTHING, db_column='provider_oid')

    class Meta:
        managed = False
        db_table = 'packages'


class Pois(models.Model):
    oid = models.UUIDField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    point = models.TextField(blank=True, null=True)  # This field type is a guess.
    polygon = models.TextField(blank=True, null=True)  # This field type is a guess.
    info = models.JSONField()
    tags = models.TextField(blank=True, null=True)  # This field type is a guess.
    public = models.BooleanField()
    multipolygon = models.TextField(blank=True, null=True)  # This field type is a guess.
    visible = models.BooleanField()
    company_oid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_oid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pois'
        unique_together = (('name', 'company_oid'),)


class Products(models.Model):
    name = models.CharField(max_length=255)
    properties = models.JSONField()

    class Meta:
        managed = False
        db_table = 'products'


class Providers(models.Model):
    oid = models.UUIDField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    prices = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'providers'


class Queue(models.Model):
    id = models.BigAutoField(primary_key=True)
    enqueued_at = models.DateTimeField()
    dequeued_at = models.DateTimeField(blank=True, null=True)
    expected_at = models.DateTimeField(blank=True, null=True)
    schedule_at = models.DateTimeField(blank=True, null=True)
    q_name = models.TextField()
    data = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'queue'


class QueuesStatus(models.Model):
    oid = models.UUIDField(primary_key=True)
    name = models.TextField()
    ts = models.DateTimeField()
    packages = models.IntegerField(blank=True, null=True)
    workers = models.IntegerField(blank=True, null=True)
    time_processing_average = models.DurationField(blank=True, null=True)
    time_deq_enq_average = models.DurationField(blank=True, null=True)
    population_time_deq_enq = models.IntegerField(blank=True, null=True)
    pending_jobs = models.IntegerField(blank=True, null=True)
    interval_enqueue = models.DurationField(blank=True, null=True)
    overwhelmed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'queues_status'


class Roles(models.Model):
    role_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class RolesUserCompany(models.Model):
    oid = models.UUIDField(primary_key=True)
    company_oid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_oid')
    user_oid = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_oid')
    permissions = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    role = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_user_company'
        unique_together = (('company_oid', 'user_oid'),)


class RolesUserGroup(models.Model):
    oid = models.UUIDField(primary_key=True)
    group_oid = models.ForeignKey(Groups, models.DO_NOTHING, db_column='group_oid')
    user_oid = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_oid')
    permissions = models.TextField()  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_user_group'
        unique_together = (('group_oid', 'user_oid'),)


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Telemetrics(models.Model):
    oid = models.UUIDField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    ts = models.DateTimeField()
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    tracker_oid = models.ForeignKey('Trackers', models.DO_NOTHING, db_column='tracker_oid')
    info = models.JSONField()
    distance_prev_point = models.FloatField(blank=True, null=True)
    time_prev_point = models.FloatField(blank=True, null=True)
    point_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    geojson = models.TextField(blank=True, null=True)  # This field type is a guess.
    event_code = models.ForeignKey(Events, models.DO_NOTHING, db_column='event_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telemetrics'
        unique_together = (('oid', 'ts'),)


class TrackerCredential(models.Model):
    oid = models.UUIDField(primary_key=True)
    tracker_oid = models.ForeignKey('Trackers', models.DO_NOTHING, db_column='tracker_oid')
    credential_oid = models.ForeignKey(Credentials, models.DO_NOTHING, db_column='credential_oid')

    class Meta:
        managed = False
        db_table = 'tracker_credential'


class TrackerDocuments(models.Model):
    oid = models.UUIDField(primary_key=True)
    created_at = models.DateTimeField()
    tracker_oid = models.ForeignKey('Trackers', models.DO_NOTHING, db_column='tracker_oid')
    user_oid = models.ForeignKey('Users', models.DO_NOTHING, db_column='user_oid')
    file_name = models.TextField(unique=True)
    file_format = models.TextField(blank=True, null=True)  # This field type is a guess.
    status = models.TextField()  # This field type is a guess.
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracker_documents'


class TrackerPackages(models.Model):
    tracker_oid = models.OneToOneField('Trackers', models.DO_NOTHING, db_column='tracker_oid', primary_key=True)
    package_oid = models.ForeignKey(Packages, models.DO_NOTHING, db_column='package_oid')

    class Meta:
        managed = False
        db_table = 'tracker_packages'
        unique_together = (('tracker_oid', 'package_oid'),)


class TrackerProperties(models.Model):
    oid = models.UUIDField(primary_key=True)
    tracker_oid = models.ForeignKey('Trackers', models.DO_NOTHING, db_column='tracker_oid')
    key = models.TextField()  # This field type is a guess.
    value = models.FloatField(blank=True, null=True)
    ts = models.DateTimeField()
    extra_info = models.JSONField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracker_properties'
        unique_together = (('oid', 'ts'),)


class TrackerPropertyKeys(models.Model):
    key_name = models.CharField(unique=True, max_length=50)
    info = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracker_property_keys'


class TrackerRecords(models.Model):
    oid = models.UUIDField(primary_key=True)
    tracker_oid = models.OneToOneField('Trackers', models.DO_NOTHING, db_column='tracker_oid')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    odometer = models.FloatField(blank=True, null=True)
    ts_odometer = models.DateTimeField(blank=True, null=True)
    ignition = models.FloatField(blank=True, null=True)
    ts_ignition = models.DateTimeField(blank=True, null=True)
    speed = models.FloatField(blank=True, null=True)
    ts_speed = models.DateTimeField(blank=True, null=True)
    consumption = models.JSONField()
    binary = models.JSONField()
    tires = models.JSONField()
    ts_consumption = models.DateTimeField(blank=True, null=True)
    ts_binary = models.DateTimeField(blank=True, null=True)
    ts_tires = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tracker_records'


class Trackers(models.Model):
    oid = models.UUIDField(primary_key=True)
    tracker_id = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=255)  # This field type is a guess.
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    object_id = models.JSONField()
    heartbeat = models.DateTimeField()
    geom = models.CharField(blank=True, null=True, max_length=255)  # This field type is a guess.
    latitude = models.CharField(blank=True, null=True, max_length=255)
    longitude = models.CharField(blank=True, null=True, max_length=255)
    external_validation_data = models.JSONField(blank=True, null=True)
    foreign_tracker_id = models.CharField(blank=True, null=True, max_length=255)
    validation_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    company_oid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_oid', blank=True, null=True)
    moving = models.BooleanField()
    locked = models.BooleanField()
    status = models.BooleanField()
    billed_date = models.DateTimeField(blank=True, null=True)
    schedule_oid = models.ForeignKey('TrackingSchedules', models.DO_NOTHING, db_column='schedule_oid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trackers'



class TrackingSchedules(models.Model):
    schedule = models.JSONField()
    timezone = models.CharField(max_length=255)
    company_oid = models.UUIDField(blank=True, null=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    oid = models.UUIDField(unique=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'tracking_schedules'

class Trips(models.Model):
    oid = models.UUIDField(primary_key=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.
    tracker_oid = models.ForeignKey(Trackers, models.DO_NOTHING, db_column='tracker_oid')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    end_address = models.JSONField(blank=True, null=True)
    start_address = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    computed_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    geojson = models.JSONField()
    points_oid = models.TextField(blank=True, null=True)  # This field type is a guess.
    vertex_number = models.IntegerField(blank=True, null=True)
    distance_by_geom = models.FloatField(blank=True, null=True)
    geom_by_mm = models.TextField(blank=True, null=True)  # This field type is a guess.
    distance_by_odometer = models.FloatField(blank=True, null=True)
    distance_by_mm_geom = models.FloatField(blank=True, null=True)
    avg_speed_by_mm_geom = models.FloatField(blank=True, null=True)
    avg_speed_by_odometer = models.FloatField(blank=True, null=True)
    avg_speed_by_geom = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trips'
        unique_together = (('oid', 'start_date', 'tracker_oid'),)


class UserInvitations(models.Model):
    oid = models.UUIDField(primary_key=True)
    company_oid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='company_oid')
    email = models.TextField(unique=True)
    roles = models.JSONField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_invitations'
        unique_together = (('company_oid', 'email'),)


class Users(models.Model):
    oid = models.UUIDField(primary_key=True)
    fullname = models.TextField()
    email = models.TextField(unique=True)
    password = models.TextField()
    validated = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
    admin = models.BooleanField(blank=True, null=True)
    recover_password_token = models.TextField(blank=True, null=True)
    recover_password_token_expiration_date = models.DateTimeField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    dashboard = models.JSONField(blank=True, null=True)
    job_title = models.TextField(blank=True, null=True)
    active_company = models.UUIDField(blank=True, null=True)
    has_accepted_marketing_contact = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'users'


class VehicleMakes(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vehicle_makes'


class VehicleModels(models.Model):
    oid = models.UUIDField(primary_key=True)
    name = models.TextField(unique=True)
    manufacturer = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)
    info = models.JSONField(blank=True, null=True)
    countries_alias = models.JSONField()

    class Meta:
        managed = False
        db_table = 'vehicle_models'


class VehicleModelsMakes(models.Model):
    name = models.CharField(max_length=255)
    make = models.ForeignKey(VehicleMakes, models.DO_NOTHING)
    vehicle_type = models.ForeignKey('VehicleTypes', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vehicle_models_makes'


class VehicleTypes(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vehicle_types'
