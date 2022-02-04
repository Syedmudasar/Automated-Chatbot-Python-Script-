from com_hrbot_constant.constant import Constant
from com_htbot_utility.utility import Utility

class HrBot_Config_mapper:

    hrbot_config = Utility.config_selection_map(Utility.get_data(Constant.hrbot_config)[0])

    hrbot_locators = Utility.config_selection_map(Utility.get_data(Constant.hrbot_locators)[1])

    add_title_name = HrBot_Config_mapper.hrbot_locators.get('add_title_name')


