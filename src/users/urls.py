from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserRegisterForm, UserLoginForm, ChangePassForm, ResetPassForm, SetPassForm, MemberCreationForm
from registration.backends.default.views import RegistrationView, ActivationView
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^home/$', views.home, name="home"),
    # Register, Login, edit password urls (Django auth)
    url(r'^register/$', RegistrationView.as_view(form_class = UserRegisterForm), name = 'register'),
    url(r'^login/$', auth_views.login, {'authentication_form': UserLoginForm}, name = 'auth_login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='auth_logout'),
    url(r'^password/change/$', auth_views.password_change, {'password_change_form': ChangePassForm}, name='auth_password_change'),
    url(r'^password_change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', auth_views.password_reset, {'password_reset_form': ResetPassForm}, name='auth_password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, {'set_password_form': SetPassForm}, name='auth_password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^activate/complete/$', TemplateView.as_view(template_name='registration/activation_complete.html'), name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$', ActivationView.as_view(), name='registration_activate'),
    url(r'^register/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
    url(r'^register/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'), name='registration_disallowed'),
    # User urls
    url(r'^user/list/$', views.user_list, name="user_list"),
    url(r'^user/edit/(?P<id>\d+)/$', views.user_edit, name="user_edit"),
    # Profile urls (Editors, Organizers...)
    url(r'^profile/edit/(?P<id>\d+)/$', views.profile_edit, name="profile_edit"),
    url(r'^profile/creation/$', views.Backend.as_view(form_class = MemberCreationForm,template_name='registration/registration_form_email.html'), name="profile_creation"),
    # Dataset urls
    url(r'^dataset/list/$', views.dataset_list, name="dataset_list"),
    url(r'^dataset/creation/$', views.dataset_creation, name="dataset_creation"),
    url(r'^dataset/(?P<id>\d+)/edit/$', views.dataset_edit, name="dataset_edit"),
    url(r'^dataset/(?P<id>\d+)/publish/$', views.dataset_publish, name="dataset_publish"),
    url(r'^dataset/(?P<id>\d+)/unpublish/$', views.dataset_unpublish, name="dataset_unpublish"),
    url(r'^dataset/(?P<id>\d+)/description/$', views.dataset_desc, name="dataset_desc"),
    url(r'^dataset/(?P<id>\d+)/schedule/$', views.dataset_schedule, name="dataset_schedule"),
    url(r'^dataset/(?P<id>\d+)/remove/$', views.dataset_remove, name="dataset_remove"),
    # url(r'^dataset/select/(?P<id>\d+)/$', views.dataset_select, name="dataset_select"),
    # Data urls
    url(r'^dataset/(?P<id>\d+)/data/creation/$', views.data_creation, name="data_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/remove/$', views.data_remove, name="data_remove"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/description/$', views.data_desc, name="data_desc"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/software/$', views.data_software, name="data_software"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/files/$', views.data_files, name="data_files"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/metric/$', views.data_metric, name="data_metric"),
    url(r'^dataset/(?P<dataset_id>\d+)/results/$', views.dataset_results, name="dataset_results"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/edit/$', views.data_edit, name="data_edit"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/file/creation/$', views.file_creation, name="file_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/data/(?P<id>\d+)/file/(?P<file_id>\d+)/remove/$', views.file_remove, name="file_remove"),
    url(r'^dataset/(?P<dataset_id>\d+)/schedule/creation$', views.schedule_creation, name="schedule_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/schedule/(?P<schedule_id>\d+)/edit/$', views.schedule_edit, name="schedule_edit"),
    url(r'^dataset/(?P<dataset_id>\d+)/schedule/(?P<schedule_id>\d+)/remove/$', views.dataset_schedule_remove, name="dataset_schedule_remove"),
    url(r'^dataset/(?P<dataset_id>\d+)/associated-events/creation$', views.event_relation_creation, name="dataset_associated_events_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/associated-events/(?P<relation_id>\d+)/remove$', views.event_relation_remove, name="dataset_associated_events_remove"),
    url(r'^dataset/(?P<dataset_id>\d+)/associated-events/$', views.dataset_associated_events, name="dataset_associated_events"),
    url(r'^dataset/(?P<dataset_id>\d+)/news/creation/$', views.news_creation, name="dataset_news_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/news/(?P<news_id>\d+)/remove$', views.dataset_news_remove, name="dataset_news_remove"),
    url(r'^dataset/(?P<dataset_id>\d+)/submission/creation$', views.submission_creation, name="submission_creation"),
    url(r'^dataset/(?P<dataset_id>\d+)/member/select/$', views.dataset_profile_select, name="dataset_profile_select"),
    url(r'^dataset/(?P<dataset_id>\d+)/member/(?P<member_id>\d+)/remove$', views.dataset_member_remove, name="dataset_member_remove"),
    # Partner urls
    url(r'^partner/list/$', views.partner_list, name="partners_list"),
    url(r'^partner/creation/$', views.partner_creation, name="partner_creation"),
    url(r'^partner/select/(?P<id>\d+)/$', views.partner_select, name="partner_select"),
    # Event urls (Challenge, Workshops...)
    url(r'^event/list/$', views.event_list, name="event_list"),
    url(r'^event/creation/$', views.event_creation, name="event_creation"),
    url(r'^event/(?P<id>\d+)/remove/$', views.event_remove, name="event_remove"),
    url(r'^event/(?P<id>\d+)/member/select/$', views.profile_select, name="profile_select"),
    url(r'^event/(?P<id>\d+)/member/(?P<member_id>\d+)/remove$', views.event_member_remove, name="event_member_remove"),
    url(r'^event/(?P<id>\d+)/news/(?P<news_id>\d+)/remove$', views.event_news_remove, name="event_news_remove"),
    url(r'^event/(?P<id>\d+)/program/(?P<program_id>\d+)/remove$', views.event_program_remove, name="event_program_remove"),
    url(r'^event/(?P<id>\d+)/schedule/(?P<program_id>\d+)/remove$', views.event_program_remove, name="event_schedule_remove"),
    url(r'^event/(?P<id>\d+)/partner/(?P<partner_id>\d+)/remove$', views.event_partner_remove, name="event_partner_remove"),
    url(r'^event/(?P<id>\d+)/associated-events/creation$', views.event_relation_creation, name="event_relation_creation"),
    url(r'^event/(?P<id>\d+)/associated-events/(?P<relation_id>\d+)/remove$', views.event_relation_remove, name="event_relation_remove"),
    url(r'^event/(?P<id>\d+)/associated-events/(?P<relation_id>\d+)/edit$', views.event_relation_edit, name="event_relation_edit"),
    url(r'^event/(?P<id>\d+)/news/creation/$', views.news_creation, name="news_creation"),
    url(r'^event/(?P<id>\d+)/news/edit/$', views.news_edit, name="news_edit"),
    url(r'^event/(?P<id>\d+)/program/creation/$', views.program_creation, name="program_creation"),
    url(r'^event/(?P<event_id>\d+)/schedule/(?P<schedule_id>\d+)/edit/$', views.schedule_edit, name="schedule_edit"),
    url(r'^event/(?P<event_id>\d+)/program/(?P<program_id>\d+)/subevent/creation/$', views.subevent_creation, name="subevent_creation"),
    url(r'^event/(?P<event_id>\d+)/schedule/creation$', views.schedule_creation, name="schedule_creation"),
    # url(r'^event/edit/(?P<id>\d+)/$', views.event_edit, name="event_edit"),
    # url(r'^event/proposal/$', views.event_proposal, name="event_proposal"),
    url(r'^challenge/(?P<id>\d+)/publish/$', views.challenge_publish, name="challenge_publish"),
    url(r'^challenge/(?P<id>\d+)/unpublish/$', views.challenge_unpublish, name="challenge_unpublish"),
    url(r'^challenge/(?P<id>\d+)/edit/$', views.challenge_edit, name="challenge_edit"),
    url(r'^challenge/(?P<id>\d+)/description/$', views.challenge_desc, name="challenge_desc"),
    url(r'^challenge/(?P<id>\d+)/people/$', views.challenge_members, name="challenge_members"),
    url(r'^challenge/(?P<id>\d+)/sponsors/$', views.challenge_sponsors, name="challenge_sponsors"),
    url(r'^challenge/(?P<id>\d+)/result/$', views.challenge_result, name="challenge_result"),
    url(r'^challenge/(?P<id>\d+)/schedule/$', views.challenge_schedule, name="challenge_schedule"),
    url(r'^challenge/(?P<id>\d+)/associated-events/$', views.challenge_associated_events, name="challenge_associated_events"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/remove$', views.track_remove, name="track_remove"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/edit$', views.track_edit, name="track_edit"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/description/$', views.track_desc, name="track_desc"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/metrics/$', views.track_metrics, name="track_metrics"),
    url(r'^challenge/(?P<id>\d+)/track/(?P<track_id>\d+)/baseline/$', views.track_baseline, name="track_baseline"),
    url(r'^challenge/(?P<id>\d+)/track/creation/$', views.track_creation, name="track_creation"),
    url(r'^workshop/(?P<id>\d+)/publish/$', views.workshop_publish, name="workshop_publish"),
    url(r'^workshop/(?P<id>\d+)/unpublish/$', views.workshop_unpublish, name="workshop_unpublish"),
    url(r'^workshop/(?P<id>\d+)/edit/$', views.workshop_edit, name="workshop_edit"),
    url(r'^workshop/(?P<id>\d+)/description/$', views.workshop_desc, name="workshop_desc"),
    url(r'^workshop/(?P<id>\d+)/program/$', views.workshop_program, name="workshop_program"),
    url(r'^workshop/(?P<id>\d+)/schedule/$', views.workshop_schedule, name="workshop_schedule"),
    url(r'^workshop/(?P<id>\d+)/associated-events/$', views.workshop_associated_events, name="workshop_associated_events"),
    url(r'^workshop/(?P<id>\d+)/speakers/$', views.workshop_speakers, name="workshop_speakers"),
    url(r'^workshop/(?P<id>\d+)/gallery/$', views.workshop_gallery, name="workshop_gallery"),
    url(r'^workshop/(?P<id>\d+)/gallery/add$', views.add_gallery_picture, name="add_gallery_picture"),
    url(r'^workshop/(?P<id>\d+)/speaker/creation$', views.speaker_creation, name="speaker_creation"),
    url(r'^workshop/(?P<id>\d+)/speaker/select$', views.speaker_select, name="speaker_select"),
    url(r'^specialissue/(?P<id>\d+)/publish/$', views.special_issue_publish, name="special_issue_publish"),
    url(r'^specialissue/(?P<id>\d+)/unpublish/$', views.special_issue_unpublish, name="special_issue_unpublish"),
    url(r'^specialissue/(?P<id>\d+)/edit/$', views.special_issue_edit, name="special_issue_edit"),
    url(r'^specialissue/(?P<id>\d+)/description/$', views.special_issue_desc, name="special_issue_desc"),
    url(r'^specialissue/(?P<id>\d+)/people/$', views.special_issue_members, name="special_issue_members"),
    url(r'^specialissue/(?P<id>\d+)/schedule/$', views.special_issue_schedule, name="special_issue_schedule"),
    url(r'^specialissue/(?P<id>\d+)/associated-events/$', views.special_issue_associated_events, name="special_issue_associated_events"),
    # Role urls
    url(r'^role/creation/$', views.role_creation, name="role_creation"),
    url(r'^event-proposal/creation/$', views.event_proposal_creation, name="event_proposal_creation"),
    url(r'^event-proposal/list/$', views.event_proposal_list, name="event_proposal_list"),
    url(r'^event-proposal/(?P<id>\d+)/detail/$', views.event_proposal_detail, name="event_proposal_detail"),
    url(r'^event-proposal/(?P<id>\d+)/confirm/$', views.event_proposal_confirm, name="event_proposal_confirm"),
    # Schedule event urls
    # url(r'^schedule/creation/(?P<id>\d+)/$', views.schedule_creation, name="schedule_creation"),
    # url(r'^schedule/creation/(?P<workshop_id>\d+)/(?P<event_id>\d+)/subevent$', views.subevent_creation, name="subevent_creation"),
    # url(r'^schedule/edit/(?P<id>\d+)/$', views.schedule_edit, name="schedule_edit"),
]