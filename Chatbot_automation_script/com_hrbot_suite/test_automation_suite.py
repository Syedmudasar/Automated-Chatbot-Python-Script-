# from analytics_module.test_verify_url import Test1
from analytics_module.test_verify_url import Test1
from analytics_module.test_verify_elements_onlogin import Test2
from analytics_module.test_verify_login_functionality import Test3
from analytics_module.test_verify_alert_message import Test4
from analytics_module.test_verify_password_visible import Test7
from analytics_module.test_verify_alert_message_blank_credential import Test6
from analytics_module.test_verify_content_home_page import Test5
from user_management.test_verify_user_page import Test8
from user_management.test_verify_active_tab import Test9
from user_management.test_verify_all_tabs_displayed import Test13
from user_management.test_verify_deactivate_tab import Test10
from user_management.test_verify_invalidate_functionality import Test15
from user_management.test_verify_invite_tab import Test11
from user_management.test_verify_action_functionality import Test14
from user_management.test_verify_total_users_tab import Test12
from user_management.test_verify_users_data_respectively import Test26
from user_management.test_verify_resend_invitation_functionality import Test17
from user_management.test_verify_quick_action_link import Test29
from user_management.test_verify_pagination import Test31
from user_management.test_verify_invitation_functionality_by_invalid_email import Test20
from user_management.test_verify_error_message_mail_as_blank import Test19
from user_management.test_verify_content_user_invite_popup import Test18
from user_management.test_verify_invitation_functionality import Test21
from user_management.test_verify_quick_action import Test28
from user_management.test_verify_activate_profile_under_deactivate import Test16
from user_management.test_verify_editor_able_to_see_information import Test22
from user_management.test_verify_invitation_mail_sent import Test23
from user_management.test_verify_invitation_mail_sent import Test24
from user_management.test_verify_user_setting_disable import Test33
from user_management.test_verify_edit_user_profile import Test30
from central_repository.test_verify_central_repository_page import Test32
from central_repository.test_verify_content_template_page import Test38
from central_repository.test_verify_error_message import Test39
from central_repository.test_verify_FAQ_repository import Test35
from central_repository.test_verify_new_interaction_button import Test36
from central_repository.test_verify_template_screen import Test37
from analytics_module.conftest import *
import pytest


class TestSuite:
    def test_suite(self):
        Test2()
        Test1()
        Test3()
        Test4()
        Test6()
        Test7()
        Test5()
        Test8()
        Test9()
        Test10()
        Test13()
        Test15()
        Test11()
        Test14()
        Test12()
        Test16()
        Test17()
        Test18()
        Test19()
        Test20()
        Test21()
        Test22()
        Test23()
        Test24()
        Test26()
        Test28()
        Test29()
        Test30()
        Test31()
        Test32()
        Test33()
        Test35()
        Test36()
        Test37()
        Test38()
        Test39()
