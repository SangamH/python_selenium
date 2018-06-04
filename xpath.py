xpath_list = {

    "login_link": ".//a[@class='sign-in']",
    "login_email": ".//input[@id='username']",
    "login_password": ".//input[@id='password']",
    "login_button": ".//fieldset[@form='sign_in_form']/button",
    "create_survey": "//div[@id='hd']/div/a[1]",
    "survey_title": "//input[@id='newName']",
    "survey_category": "//select[@id='newCategory']",
    "go_button": "//a[contains(@class, 's1continue')]",
    "enter_question": ".//div[@id='editTitle']",
    "matrix_row_options": ".//table[@id='rows']/tbody/tr[@class='choice new']/td[1]/div[1]/div[1]",
    "choice_answer_options": ".//table[@class='answersTable choicesTable']/tbody/tr[@class='choice new']/td[2]/div[1]/div[1]",
    "add_answer_option": ".//table[@id='rows']/tbody/tr[3]/td[3]/a[1]",
    "matrix_add_answer_option": ".//table[@id='rows']/tbody/tr[3]/td[2]/a[1]",
    "save_question": ".//div[@id='editQuestion']/section[2]/div[3]/a[3]",
    "option_choice": [
        ".//div[@id='columnsWrap']/div/table/tbody/tr[2]/td[1]/div/div",
        ".//div[@id='columnsWrap']/div/table/tbody/tr[3]/td[1]/div/div",
        ".//div[@id='columnsWrap']/div/table/tbody/tr[4]/td[1]/div/div",
        ".//div[@id='columnsWrap']/div/table/tbody/tr[5]/td[1]/div/div",
        ".//div[@id='columnsWrap']/div/table/tbody/tr[6]/td[1]/div/div",
    ],
    "btn_remove_option": ".//tbody[contains(@class, 'columnSetting')]/tr[6]/td[@class='choiceActions']/a[2]",
    "page_title_clickbox": "//header[@class='survey-page-header']/div[2]",
    "page_title": ".//div[@id='pageTitle']",
    "save_page_title": ".//form[@id='pageTitleForm']/div[3]/a[1]",
    "question_suggestion": ".//input[@id='suggestQ']",
    "time_info": ".//input[@id='toggleTimeVisible']",
    "end_survey_next": ".//a[@id='sendSurvey']",
    "survey_link": ".//input[@id='weblink-url']",
    "login_page_xpath_user_name": "//input[@id='username']",
    "login_page_xpath_password": "//input[@id='password']",
    "login_page_xpath_login_btn": "//button[contains(text(),'LOG')]",
    "create_survey_btn": "//div[@id='hd']/div/div/a[2]",
    "create_survey_from_scratch_btn": "//button[@id='scratch']",
    "create_survey_title_field": "//div/input[@id='surveyTitle']",
    "create_survey_submit_btn": "//button[@class='wds-button'][contains(text(),'CREATE')]",
    "my_survery_list_btn": "//li/a[contains(text(),'My Surveys')]",
    "survey_design_btn": "//ul/li/a[contains(text(), 'DESIGN')]",
    "title_field_for_survey_question": "//div[@id='editTitle'][@data-id='editTitle']",
    "multiple_question_type_for_survey_question": "//div[contains(@id,'newChoice')]",
    "survey_question_save_btn": "//div[@id='editQuestion']//section[contains(@class, 't1')]//div[contains(@class, 'buttons')]/a[contains(@class,'save')]",
    "signup_page_xpath_user_name": "//input[@id='username']",
    "signup_page_xpath_password": "//input[@id='password']",
    "signup_page_xpath_fname": "//input[@name='first_name']",
    "signup_page_xpath_lname": "//input[@name='last_name']",
    "dropdown_question_type": "//ul[@class='add-q-menu-right']//li/div/a[contains(text(),'Dropdown')]",
    "changeQType": "//a[@id='changeQType']",
}

surveyBuilder_Xpath_List = {

    "q_multiple_choice": ".//li[@rel='MultipleChoice']",
    "q_dropdown": ".//li[@rel='Dropdown']",
    "q_rating_scale": ".//li[@rel='Matrix']",
    "q_net_promote": ".//li[@rel='QB-net_promoter_score']",
    "net_promote_option_list": ".//a[@class='faux_dropdown']",
    "net_promote_select_option": ".//ul[@view-role='qbActionMenuView']/li[4]/a",
    "q_single_textbox": ".//li[@rel='SingleTextbox']",
    "q_multiple_textboxes": ".//li[@rel='MultipleTextbox']",
    "q_comment_box": ".//li[@rel='CommentBox']",
    "q_date_time": ".//li[@rel='DateTime']",
}

globle_browser = "chrome"
log_file_title = "log_file"