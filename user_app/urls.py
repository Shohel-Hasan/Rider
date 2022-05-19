from django.urls import path, include
from .views import *
from . import views

app_name = 'user_app'

urlpatterns = [
    path('registration', view=views.UserRegisterView.as_view(), name='signup'),
    path('signin', ObtainAuthToken.as_view(), name='sign-in'),
    path('token-check', TokenCheck.as_view(), name='token'),
    path('verify-otp', UserOTPVerifyView.as_view(), name="otp_verify"),
    path('signout', view=views.Signout.as_view(), name='signout'),
    path('change-password', view=ChangePasswordView.as_view(), name='change-password'),
    path('forget-password', view=ForgetPasswordView.as_view(), name='forget-password'),
    path('reset-password', view=ResetPasswordView.as_view(), name='reset-password'),
    path('get-users', views.AllUsersViewSet.as_view({'get': 'list'}), name="users"),
    path('<int:user_id>', views.SingleUserInfoViewSet.as_view({'get': 'retrieve'}), name="users"),

    path('user-general-info', UserGeneralInfoCreateView.as_view(), name='user-general-info'),
    path('user-general-info/<int:id>', UserGeneralInfoGetView.as_view(),
         name='user-general-info-get'),
    path('user-general-info-update/<int:user_id>', UserGeneralInfoUpdateView.as_view({'put': 'patch'}),
         name='user-general-info-update'),
    path('user-general-info-view-hide/<int:id>/',
         UserGeneralInfoViewHideView.as_view(),
         name='user-general-info-view-hide'),
    path('user-name-update/<int:id>/', UserNameUpdateView.as_view(),
         name='user-name-update'),

    path('user-contact-info', UserContactInfoCreateView.as_view(), name='user-contact-info'),
    path('user-contact-info/<int:id>', UserContactInfoGetView.as_view(),
         name='user-contact-info-get'),
    path('user-contact-info-update/<int:user_id>', UserContactInfoUpdateView.as_view({'put': 'patch'}),
         name='user-contact-info-update'),
    path('user-contact-info-view-hide/<int:id>/',
         UserContactInfoViewHideView.as_view()),

    path('user-language-proficiency', UserLanguageProficiencyCreateView.as_view(), name='user-language-proficiency'),
    path('user-language-proficiency/<int:user_id>', UserLanguageProficiencyGetView.as_view({'get': 'list'}),
         name='user-language-proficiency-get'),
    path('user-language-proficiency-update/<int:user_id>/<int:contact_id>',
         UserLanguageProficiencyUpdateView.as_view({'put': 'patch'}),
         name='user-language-proficiency-update'),
    path('user-language-proficiency-delete/<int:user_id>/<int:language_proficiency_id>',
         UserLanguageProficiencyDeleteView.as_view({'delete': 'destroy'}),
         name='user-language-proficiency-delete'),
    path('user-language-view-hide/<int:id>/',
         UserLanguageProficiencyViewHideView.as_view(),
         name='user-language-view-hide'),

    path('user-language-score', UserLanguageScoreCreateView.as_view(), name='user-language-score'),
    path('user-language-score/<int:user_id>', UserLanguageScoreGetView.as_view({'get': 'list'}),
         name='user-language-score-get'),
    path('user-language-score-update/<int:user_id>/<int:score_id>',
         UserLanguageScoreUpdateView.as_view({'put': 'patch'}),
         name='user-language-score-update'),
    path('user-language-score-delete/<int:user_id>/<int:score_id>',
         UserLanguageScoreDeleteView.as_view({'delete': 'destroy'}),
         name='user-language-score-delete'),
    path('user-language-score-view-hide/<int:id>/',
         UserLanguageScoreViewHideView.as_view(),
         name='user-language-score-view-hide'),
    path('user-research-skill', UserResearchSkillCreateView.as_view(), name='user-research-skill'),
    path('user-research-skill/<int:user_id>', UserResearchSkillGetView.as_view(),
         name='user-research-skill-get'),
    path('user-research-skill-update/<int:user_id>',
         UserResearchSkillUpdateView.as_view({'put': 'patch'}),
         name='user-research-skill-update'),
    path('user-research-skill-delete/<int:user_id>/<int:score_id>',
         UserResearchSkillDeleteView.as_view({'delete': 'destroy'}),
         name='user-research-skill-delete'),
    path('user-research-skill-view-hide/<int:id>/',
         UserResearchSkillViewHideView.as_view(),
         name='user-research-skill-view-hide'),

    path('user-research-article', UserResearchArticleCreateView.as_view(), name='user-research-article'),
    path('user-research-article/<int:user_id>', UserResearchArticleGetView.as_view({'get': 'list'}),
         name='user-research-article'),
    path('user-research-article-update/<int:user_id>/<int:article_id>',
         UserResearchArticleUpdateView.as_view({'put': 'patch'}),
         name='user-research-article-update'),
    path('user-research-article-delete/<int:user_id>/<int:article_id>',
         UserResearchArticleDeleteView.as_view({'delete': 'destroy'}),
         name='user-research-article-delete'),
    path('user-research-article-view-hide/<int:id>/',
         UserResearchArticleViewHideView.as_view(),
         name='user-research-article-view-hide'),

    path('user-research-work', UserResearchWorkCreateView.as_view(), name='user-research-work'),
    path('user-research-work/<int:user_id>', UserResearchWorkGetView.as_view({'get': 'list'}),
         name='user-research-work-get'),
    path('user-research-work-update/<int:user_id>/<int:work_id>',
         UserResearchWorkUpdateView.as_view({'put': 'patch'}),
         name='user-research-work-update'),
    path('user-research-work-delete/<int:user_id>/<int:work_id>',
         UserResearchWorkDeleteView.as_view({'delete': 'destroy'}),
         name='user-research-work-delete'),
    path('user-research-work-view-hide/<int:id>/',
         UserResearchWorkViewHideView.as_view(),
         name='user-research-work-view-hide'),

    path('user-research-summary', UserResearchSummaryCreateView.as_view(), name='user-research-summary'),
    path('user-research-summary/<int:user_id>', UserResearchSummaryGetView.as_view({'get': 'list'}),
         name='user-research-summary-get'),
    path('user-research-summary-update/<int:user_id>/<int:summary_id>',
         UserResearchSummaryUpdateView.as_view({'put': 'patch'}),
         name='user-research-summary-update'),
    path('user-research-summary-delete/<int:user_id>/<int:summary_id>',
         UserResearchSummaryDeleteView.as_view({'delete': 'destroy'}),
         name='user-research-summary-delete'),
    path('user-research-summary-view-hide/<int:id>/',
         UserResearchSummaryViewHideView.as_view(),
         name='user-research-summary-view-hide'),

    path('user-research-thoughts', UserResearchThoughtCreateView.as_view(), name='user-research-thought'),
    path('user-research-thoughts/<int:user_id>', UserResearchThoughtGetView.as_view({'get': 'list'}),
         name='user-research-thought-get'),
    path('user-research-thoughts-update/<int:user_id>/<int:thoughts_id>',
         UserResearchThoughtsUpdateView.as_view({'put': 'patch'}),
         name='user-research-thoughts-update'),
    path('user-research-thoughts-delete/<int:user_id>/<int:thoughts_id>',
         UserResearchThoughtsDeleteView.as_view({'delete': 'destroy'}),
         name='user-research-thoughts-delete'),
    path('user-research-thoughts-view-hide/<int:id>/',
         UserResearchThoughtsViewHideView.as_view(),
         name='user-research-thoughts-view-hide'),

    path('user-other-info', UserOtherInfoCreateView.as_view(), name='user-other-info'),
    path('user-other-info/<int:user_id>', UserOtherInfoGetView.as_view({'get': 'list'}),
         name='user-other-info-get'),
    path('user-other-info-update/<int:user_id>',
         UserOtherInfoUpdateView.as_view({'put': 'patch'}),
         name='user-other-info-update'),

    path('user-skill', UserSkillCreateView.as_view(), name='user-skill'),
    path('user-skill/<int:user_id>', UserSkillGetView.as_view(),
         name='user-skill-get'),
    path('user-skill-update-delete/<int:id>', UserSkillUpdateDeleteView.as_view()),

    path('user-skill-view-hide/<int:id>/',
         UserSkillViewHideView.as_view()),
    path('user-skill-update/<int:user_id>',
         UserSkillUpdateView.as_view({'put': 'patch'}),
         name='user-skill-update'),  # This path May be deleted

    path('user-working-history', UserWorkingHistoryCreateView.as_view(), name='user-working-history'),
    path('user-working-history/<int:user_id>', UserWorkingHistoryGetView.as_view({'get': 'list'}),
         name='user-working-history-get'),
    path('user-working-history-update/<int:user_id>/<int:work_history_id>',
         UserWorkingHistoryUpdateView.as_view({'put': 'patch'}),
         name='user-working-history-update'),
    path('user-working-history-delete/<int:user_id>/<int:work_history_id>',
         UserWorkingHistoryDeleteView.as_view({'delete': 'destroy'}),
         name='user-working-history-delete'),

    path('user-working-history-view-hide/<int:id>/',
         UserWorkingHistoryViewHideView.as_view(),
         name='user-working-history-view-hide'),

    path('user-academic-discipline', UserAcademicDisciplineCreateView.as_view(), name='user-academic-discipline'),
    path('user-academic-discipline/<int:user_id>', UserAcademicDisciplineGetView.as_view({'get': 'list'}),
         name='user-academic-discipline-get'),
    path('user-academic-discipline-update/<int:user_id>/<int:academic_discipline_id>',
         UserAcademicDisciplineUpdateView.as_view({'put': 'patch'}),
         name='user-academic-discipline-update'),
    path('user-academic-discipline-delete/<int:user_id>/<int:academic_discipline_id>',
         UserAcademicDisciplineDeleteView.as_view({'delete': 'destroy'}),
         name='user-academic-discipline-delete'),

    path('user-academic-discipline-view-hide/<int:id>/',
         UserAcademicDisciplineViewHideView.as_view(),
         name='user-academic-discipline-view-hide'),

    path('user-academic-degree', UserAcademicDegreeCreateView.as_view(), name='user-academic-degree'),
    path('user-academic-degree/<int:user_id>', UserAcademicDegreeGetView.as_view({'get': 'list'}),
         name='user-academic-degree-get'),
    path('user-academic-degree-update/<int:user_id>/<int:academic_degree_id>',
         UserAcademicDegreeUpdateView.as_view({'put': 'patch'}),
         name='user-academic-degree-update'),
    path('user-academic-degree-delete/<int:user_id>/<int:academic_degree_id>',
         UserAcademicDegreeDeleteView.as_view({'delete': 'destroy'}),
         name='user-academic-degree-delete'),

    path('user-academic-degree-view-hide/<int:id>/',
         UserAcademicDegreeViewHideView.as_view(),
         name='user-academic-degree-view-hide'),

    path('user-training', UserTrainingCreateView.as_view(), name='user-training'),
    path('user-training/<int:user_id>', UserTrainingGetView.as_view({'get': 'list'}),
         name='user-training-get'),
    path('user-training-update/<int:user_id>/<int:training_id>',
         UserTrainingUpdateView.as_view({'put': 'patch'}),
         name='user-training-update'),
    path('user-training-delete/<int:user_id>/<int:training_id>',
         UserTrainingDeleteView.as_view({'delete': 'destroy'}),
         name='user-training-delete'),

    path('user-training-view-hide/<int:id>/',
         UserTrainingViewHideView.as_view(),
         name='user-training-view-hide'),

    path('user-workshop-or-seminar', UserWorkshopSeminarCreateView.as_view(), name='user-workshop-or-seminar'),
    path('user-workshop-or-seminar/<int:user_id>', UserWorkshopSeminarGetView.as_view({'get': 'list'}),
         name='user-workshop-or-seminar-get'),
    path('user-workshop-or-seminar-update/<int:user_id>/<int:workshop_seminar_id>',
         UserWorkshopOrSeminarUpdateView.as_view({'put': 'patch'}),
         name='user-workshop-or-seminar-update'),
    path('user-workshop-or-seminar-delete/<int:user_id>/<int:workshop_seminar_id>',
         UserWorkshopOrSeminarDeleteView.as_view({'delete': 'destroy'}),
         name='user-workshop-or-seminar-delete'),

    path('user-workshop-or-seminar-view-hide/<int:id>/',
         UserWorkshopOrSeminarViewHideView.as_view(),
         name='user-workshop-or-seminar-view-hide'),
    path('user-book-publications', UserBookPublicationsView.as_view()),
    path('user-book-publications/<int:user_id>', UserBookPublicationsView.as_view()),
    path('user-book-publications-update-delete/<int:id>', UserBookPublicationsUpdateDeleteView.as_view()),
    path('user-book-publications-view-hide/<int:id>/',
         UserBookPublicationsViewHideView.as_view()),
    path('user-working-skills', UserWorkingSkillView.as_view()),
    path('user-working-skills/<int:user_id>', UserWorkingSkillView.as_view()),
    path('user-working-skills-update-delete/<int:id>', UserWorkingSkillUpdateDeleteView.as_view()),
    path('user-working-skills-view-hide/<int:id>/',
         UserWorkingSkillViewHideView.as_view()),
    path('user-academic-achievement', AcademicAchievementView.as_view()),
    path('user-academic-achievement/<int:user_id>', AcademicAchievementView.as_view()),
    path('user-academic-achievement-update-delete/<int:id>', AcademicAchievementUpdateDeleteView.as_view()),
    path('user-academic-achievement-view-hide/<int:id>/',
         AcademicAchievementViewHideView.as_view()),
    path('user-notable-achievement', NotableAchievementView.as_view()),
    path('user-notable-achievement/<int:user_id>', NotableAchievementView.as_view()),
    path('user-notable-achievement-update-delete/<int:id>', NotableAchievementUpdateDeleteView.as_view()),
    path('user-notable-achievement-view-hide/<int:id>/',
         NotableAchievementViewHideView.as_view()),

]