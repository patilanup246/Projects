import requests
import re
url = 'https://www.facebook.com/ajax/pagelet/generic.php/BrowseScrollingSetPagelet?dpr=1&data=%7B%22view%22%3A%22list%22%2C%22encoded_query%22%3A%22%7B%5C%22bqf%5C%22%3A%5C%22keywords_pages(lawyers%2BNew%2BYork%2BUnited%2BStates)%5C%22%2C%5C%22browse_sid%5C%22%3Anull%2C%5C%22vertical%5C%22%3A%5C%22content%5C%22%2C%5C%22post_search_vertical%5C%22%3Anull%2C%5C%22intent_data%5C%22%3A%5C%22%7B%5C%5C%5C%22intent%5C%5C%5C%22%3A%5C%5C%5C%22posts%5C%5C%5C%22%2C%5C%5C%5C%22entity_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22sub_intents%5C%5C%5C%22%3A%7B%5C%5C%5C%22newsy_by_nms%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22media_video%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22live%5C%5C%5C%22%3Atrue%7D%2C%5C%5C%5C%22user_confidence%5C%5C%5C%22%3A0.0032810227779759%2C%5C%5C%5C%22quel_topics%5C%5C%5C%22%3A[%7B%5C%5C%5C%22fbid%5C%5C%5C%22%3A111979848819624%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.9%2C%5C%5C%5C%22position%5C%5C%5C%22%3A8%2C%5C%5C%5C%22length%5C%5C%5C%22%3A8%7D]%2C%5C%5C%5C%22multi_label_intents%5C%5C%5C%22%3A[%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.0039955824613571%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A1.9546305338736e-5%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.015081614255905%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.053752113133669%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.0077484324574471%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.00017247170035262%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.0040825325995684%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.0041192653588951%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.011847391724586%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.071822874248028%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.31984725594521%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.029204305261374%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.20711325109005%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.56486201286316%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.016803434118629%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.00029549837927334%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.028336832299829%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.048978433012962%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.033079024404287%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.010926289483905%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D%2C%7B%5C%5C%5C%22value%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%22confidence%5C%5C%5C%22%3A0.0081801302731037%2C%5C%5C%5C%22source%5C%5C%5C%22%3Anull%7D]%2C%5C%5C%5C%22annotated_string%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22tokens%5C%5C%5C%5C%5C%5C%5C%22%3A[%5C%5C%5C%5C%5C%5C%5C%22lawyers%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22new%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22york%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22united%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22states%5C%5C%5C%5C%5C%5C%5C%22]%2C%5C%5C%5C%5C%5C%5C%5C%22entities%5C%5C%5C%5C%5C%5C%5C%22%3A%7B%5C%5C%5C%5C%5C%5C%5C%221_2%5C%5C%5C%5C%5C%5C%5C%22%3A[%7B%5C%5C%5C%5C%5C%5C%5C%22mention%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22new%20york%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22fbid%5C%5C%5C%5C%5C%5C%5C%22%3A108424279189115%2C%5C%5C%5C%5C%5C%5C%5C%22name%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22New%20York%2C%20New%20York%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22probability%5C%5C%5C%5C%5C%5C%5C%22%3A0.9%2C%5C%5C%5C%5C%5C%5C%5C%22wikiFbid%5C%5C%5C%5C%5C%5C%5C%22%3A111979848819624%2C%5C%5C%5C%5C%5C%5C%5C%22isWikiPage%5C%5C%5C%5C%5C%5C%5C%22%3Atrue%2C%5C%5C%5C%5C%5C%5C%5C%22source%5C%5C%5C%5C%5C%5C%5C%22%3A5%2C%5C%5C%5C%5C%5C%5C%5C%22type%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22LOCATION%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22fbType%5C%5C%5C%5C%5C%5C%5C%22%3A102%2C%5C%5C%5C%5C%5C%5C%5C%22isConnected%5C%5C%5C%5C%5C%5C%5C%22%3Anull%2C%5C%5C%5C%5C%5C%5C%5C%22category%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22city%5C%5C%5C%5C%5C%5C%5C%22%7D]%7D%2C%5C%5C%5C%5C%5C%5C%5C%22segments%5C%5C%5C%5C%5C%5C%5C%22%3A[%7B%5C%5C%5C%5C%5C%5C%5C%22type%5C%5C%5C%5C%5C%5C%5C%22%3Anull%2C%5C%5C%5C%5C%5C%5C%5C%22tokens%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22lawyers%5C%5C%5C%5C%5C%5C%5C%22%7D%2C%7B%5C%5C%5C%5C%5C%5C%5C%22type%5C%5C%5C%5C%5C%5C%5C%22%3Anull%2C%5C%5C%5C%5C%5C%5C%5C%22tokens%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22new%20york%20united%20states%5C%5C%5C%5C%5C%5C%5C%22%7D]%2C%5C%5C%5C%5C%5C%5C%5C%22concepts%5C%5C%5C%5C%5C%5C%5C%22%3A%7B%5C%5C%5C%5C%5C%5C%5C%223_4%5C%5C%5C%5C%5C%5C%5C%22%3A%7B%5C%5C%5C%5C%5C%5C%5C%22start%5C%5C%5C%5C%5C%5C%5C%22%3A3%2C%5C%5C%5C%5C%5C%5C%5C%22end%5C%5C%5C%5C%5C%5C%5C%22%3A4%2C%5C%5C%5C%5C%5C%5C%5C%22mention%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22united%20states%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22concept%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22country%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22probability%5C%5C%5C%5C%5C%5C%5C%22%3A0.22627046765601%7D%2C%5C%5C%5C%5C%5C%5C%5C%221_2%5C%5C%5C%5C%5C%5C%5C%22%3A%7B%5C%5C%5C%5C%5C%5C%5C%22start%5C%5C%5C%5C%5C%5C%5C%22%3A1%2C%5C%5C%5C%5C%5C%5C%5C%22end%5C%5C%5C%5C%5C%5C%5C%22%3A2%2C%5C%5C%5C%5C%5C%5C%5C%22mention%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22new%20york%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22concept%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22city%5C%5C%5C%5C%5C%5C%5C%22%2C%5C%5C%5C%5C%5C%5C%5C%22probability%5C%5C%5C%5C%5C%5C%5C%22%3A0.9%7D%7D%7D%5C%5C%5C%22%2C%5C%5C%5C%22personalized_user_name_confidence%5C%5C%5C%22%3A0.0032810227779759%2C%5C%5C%5C%22discovery_intent%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22all_intent_scores%5C%5C%5C%22%3A%7B%5C%5C%5C%22NEWS%5C%5C%5C%22%3A0.77753093361723%2C%5C%5C%5C%22FEED_SEARCH%5C%5C%5C%22%3A0.37145199456592%2C%5C%5C%5C%22PERSON_NAME%5C%5C%5C%22%3A0.0032810227779759%2C%5C%5C%5C%22GRAMMAR%5C%5C%5C%22%3A0.046390859997394%2C%5C%5C%5C%22ENTITY%5C%5C%5C%22%3A0.58111170141284%2C%5C%5C%5C%22NEEDLE%5C%5C%5C%22%3A0.68898808956146%2C%5C%5C%5C%22PUBLIC%5C%5C%5C%22%3A0.30101257562637%2C%5C%5C%5C%22COMMERCE%5C%5C%5C%22%3A0.029723023995757%2C%5C%5C%5C%22MEDIA%5C%5C%5C%22%3A0.32624876499176%2C%5C%5C%5C%22LOCATION%5C%5C%5C%22%3A0.78878593444824%2C%5C%5C%5C%22RECIPE%5C%5C%5C%22%3A0.012263374403119%2C%5C%5C%5C%22OFFENSIVE%5C%5C%5C%22%3A1.0654443030944e-5%2C%5C%5C%5C%22FOREIGN_LANG%5C%5C%5C%22%3A0.0021221823990345%2C%5C%5C%5C%22NOT_UNDERSTAND%5C%5C%5C%22%3A0.29298943281174%2C%5C%5C%5C%22REVIEW%5C%5C%5C%22%3A0.70226579904556%2C%5C%5C%5C%22HOWTO%5C%5C%5C%22%3A0.40104761719704%2C%5C%5C%5C%22POST_SEARCH%5C%5C%5C%22%3A0.99671897722202%2C%5C%5C%5C%22MEDIA_VIDEO%5C%5C%5C%22%3A0.23589042127132%2C%5C%5C%5C%22CELEBRITY%5C%5C%5C%22%3A1.9546305338736e-5%2C%5C%5C%5C%22PERSONAL%5C%5C%5C%22%3A0.015081614255905%2C%5C%5C%5C%22MEDIA_MUSIC%5C%5C%5C%22%3A0.00017247170035262%2C%5C%5C%5C%22ENTERTAINMENT%5C%5C%5C%22%3A0.0040825325995684%2C%5C%5C%5C%22POLITICS%5C%5C%5C%22%3A0.011847391724586%2C%5C%5C%5C%22SCIENCE_TECH_EDUCATION%5C%5C%5C%22%3A0.071822874248028%2C%5C%5C%5C%22HEALTH_MEDICINE_FITNESS%5C%5C%5C%22%3A0.31984725594521%2C%5C%5C%5C%22SPORTS%5C%5C%5C%22%3A0.029204305261374%2C%5C%5C%5C%22TRAVEL%5C%5C%5C%22%3A0.016803434118629%2C%5C%5C%5C%22JOB%5C%5C%5C%22%3A0.033079024404287%2C%5C%5C%5C%22UTILITIES%5C%5C%5C%22%3A0.010926289483905%2C%5C%5C%5C%22FAMILTY_RELATIONSHIP%5C%5C%5C%22%3A0.0081801302731037%2C%5C%5C%5C%22EVENT%5C%5C%5C%22%3A0.16396443545818%2C%5C%5C%5C%22PAGE%5C%5C%5C%22%3A0.16107724606991%2C%5C%5C%5C%22GROUP%5C%5C%5C%22%3A3.4787845493156e-8%2C%5C%5C%5C%22PEOPLE%5C%5C%5C%22%3A0%2C%5C%5C%5C%22PERSON_NAME_PERSONALIZE%5C%5C%5C%22%3A0.0032810227779759%2C%5C%5C%5C%22POST_SEARCH_PERSONALIZE%5C%5C%5C%22%3A0.99671897722202%2C%5C%5C%5C%22TIMELINESS%5C%5C%5C%22%3A0.60143858194351%2C%5C%5C%5C%22PEOPLE_L2%5C%5C%5C%22%3A1.092727188734e-7%2C%5C%5C%5C%22C_MUSICIAN_BAND%5C%5C%5C%22%3A0%2C%5C%5C%5C%22C_NOTABLE_PERSON%5C%5C%5C%22%3A0%2C%5C%5C%5C%22C_COMPANY_ORG%5C%5C%5C%22%3A0%2C%5C%5C%5C%22C_ENTERTAINMENT%5C%5C%5C%22%3A0.020598197355866%2C%5C%5C%5C%22C_SPORTS%5C%5C%5C%22%3A0.0073763872496784%2C%5C%5C%5C%22C_COMMERCE%5C%5C%5C%22%3A0.021257953718305%2C%5C%5C%5C%22C_PHYSICAL_PLACE%5C%5C%5C%22%3A0.05075828358531%2C%5C%5C%5C%22C_RECIPE%5C%5C%5C%22%3A0.00029521199758165%2C%5C%5C%5C%22C_COMMUNITY%5C%5C%5C%22%3A0.65130084753036%2C%5C%5C%5C%22C_OTHER%5C%5C%5C%22%3A0.89971405267715%2C%5C%5C%5C%22NEWS_ALT%5C%5C%5C%22%3A0.085049039639038%2C%5C%5C%5C%22PEOPLE_CLICK%5C%5C%5C%22%3A0.00025112800775836%2C%5C%5C%5C%22COMMERCE_GROUP%5C%5C%5C%22%3A0.33434820175171%2C%5C%5C%5C%22LIVENESS%5C%5C%5C%22%3A-10%7D%7D%5C%22%2C%5C%22filters%5C%22%3A[]%2C%5C%22has_chrono_sort%5C%22%3Afalse%2C%5C%22query_analysis%5C%22%3Anull%2C%5C%22subrequest_disabled%5C%22%3Afalse%2C%5C%22token_role%5C%22%3A%5C%22NONE%5C%22%2C%5C%22preloaded_story_ids%5C%22%3A[]%2C%5C%22extra_data%5C%22%3Anull%2C%5C%22disable_main_browse_unicorn%5C%22%3Afalse%2C%5C%22entry_point_scope%5C%22%3Anull%2C%5C%22entry_point_surface%5C%22%3Anull%7D%22%2C%22encoded_title%22%3A%22WyJsYXd5ZXJzK05ldytZb3JrK1VuaXRlZCtTdGF0ZXMiXQ%22%2C%22ref%22%3A%22unknown%22%2C%22logger_source%22%3A%22www_main%22%2C%22typeahead_sid%22%3A%22%22%2C%22tl_log%22%3Afalse%2C%22impression_id%22%3A%22a07e8a36%22%2C%22filter_ids%22%3A%7B%22226999127329906%22%3A226999127329906%2C%22103256838688%22%3A103256838688%2C%22107372362496%22%3A107372362496%2C%22440398239325176%22%3A440398239325176%2C%22172348813258565%22%3A172348813258565%2C%221089805707737394%22%3A1089805707737394%7D%2C%22experience_type%22%3A%22grammar%22%2C%22exclude_ids%22%3Anull%2C%22browse_location%22%3A%22browse_location%3Abrowse%22%2C%22trending_source%22%3Anull%2C%22reaction_surface%22%3Anull%2C%22reaction_session_id%22%3Anull%2C%22ref_path%22%3A%22%2Fsearch%2Fpages%2F%22%2C%22is_trending%22%3Afalse%2C%22topic_id%22%3Anull%2C%22place_id%22%3Anull%2C%22story_id%22%3Anull%2C%22callsite%22%3A%22browse_ui%3Ainit_result_set%22%2C%22has_top_pagelet%22%3Atrue%2C%22display_params%22%3A%7B%22crct%22%3A%22none%22%7D%2C%22cursor%22%3A%22Abq5cIhFvi2b-I-ALhKHGGDJ5nS08v8ilh7GLeh8G69GYtKV8Y3UyV7PGMpSobq8CG4C-qumBGzZZbr9HjB4b5t2tCl4BheO5AWBYWDmrBJW7JaSg6FHajIqxGbn65Cx5zcfNipio0TXcz5uCU0F-bZRyx4rxjfnZibUFcJK11ABhfV9elSxx8X2GjWsD5VHI_EmxwaKbTaz528x8hzmk93Nd4V2dixRqOyboyQhEjsgZsofwcPa8a_Yn8VIl_QW9lpuqWb5a2Jf8G86Ksse6hfvkwLukHy291j42_QyRBd19P4bLdDXf2HfnhPa9us0s4f9DbA5TyaRQZNkUzFtvDIU7-lc8N01xVFAWJP_gFe_wMtgkTNAKCwp6vJbbeRF7DfKOScXww23x6fbThYsRnZb%22%2C%22page_number%22%3A4%2C%22em%22%3Afalse%2C%22mr%22%3Afalse%2C%22tr%22%3Anull%7D&__user=100020094199433&__a=1&__dyn=7AgNeUiFo8Q9UoHSEWC5EW3mbx65-AjO0xx-bzES2N6wAxu13wHwKzEvHyodEbbxWUaEaUdUOu3e4o98bEsz8nwsUCcBwBx62q2m5EoC-UeovG2e261EDxS3C1DCK3abyUrwr8-362y5U6OU&__af=j0&__req=1t&__be=1&__pc=EXP1%3Ahome_page_pkg&__rev=3171013'
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8",
    'cache-control': "no-cache",
    'cookie': "datr=NjRyWUerrCz3s63aq1w0CNP3; locale=en_GB; sb=XjRyWdYzwYxjYiSTwiEeC26p; c_user=100020094199433; xs=50%3AgLYQldEJs7APRA%3A2%3A1500656735%3A-1%3A-1; pl=n; lu=gA; fr=0Phy2MKxpP4uq74pC.AWX30CH8oTptqP8ml1LUAAAT__Y.BZcjQ2._a.Fly.0.0.BZcjRe.; act=1500657102627%2F7; presence=EDvF3EtimeF1500659762EuserFA21B20094199433A2EstateFDutF1500659762345CEchFDp_5f1B20094199433F11CC",
    'pragma': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.72 Safari/537.36"
    }

resp = requests.request("GET", url, headers=headers)
#print resp.text
for i in re.findall ('lfloat _ohe(.*?)\?',resp.text.replace('\/','/').replace('\"','"')):
    print i.replace(r'\" href=\"','')