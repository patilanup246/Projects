# -*- coding: utf-8 -*-
import urllib.parse
from selenium import webdriver
#from openpyxl import load_workbook
import time
import sqlite3
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("--no-sandbox")
#chromeOptions.add_extension('anticaptcha.crx')
chromeOptions.add_argument("--disable-setuid-sandbox")
driver = webdriver.Chrome(executable_path ='C:\\Users\\talib\\workspace\\Projects\\chromedriver\\chromedriver.exe')
#driver = webdriver.Chrome(chrome_options=chromeOptions)
# driver.get('chrome-extension://neodgnejhhhlcdoglifbmioajmagpeci/options.html')
# driver.find_element_by_id('auto_submit_form').click()
# driver.find_element_by_name('account_key').send_keys('5f6b75f0738a1bd09cf717392c9804a3')
# driver.find_element_by_id('save').click()

# driver.get('https://www.google.nl')
# 
# 
# 
# 
# input_f = open('googling_input',encoding='utf-8').read().split('\n')
# output_f = open('googling_output','w',encoding='utf-8')
# 
# 
# 
# for row in input_f:
#     try:
#         print (row)
#     except:
#         pass
#     
# 
#     output_f.write(row+'\t')
#     output_f.flush()
#     try:
#         driver.get('https://www.google.nl/search?q='+ urllib.parse.quote(str(row), safe=''))
#         time.sleep(1)
#         
#         try:
#             output_f.write(str(driver.find_element_by_css_selector('[class="r"] a').get_attribute('href'))+'\t')
#  
#         except Exception as e:
#             print (e)
#             output_f.write('\t')
#          
#         try:
#             for i in driver.find_elements_by_css_selector('[class="ab_button"]'):
#                 if i.text ==  'Website':
#                     
#                     output_f.write(str(i.get_attribute('href'))+'\t')
#                     break
#         except:
#             output_f.write('\t')
#           
# #         try:
# #             output_f.write(str(driver.find_element_by_css_selector('._b1m.kp-hc a.ab_button[role="button"]').get_attribute('href'))+'\t')
# #         except:
# #             output_f.write('\t')
# #           
# #         try:
# #             output_f.write(str(driver.find_element_by_css_selector('[class="_Xbe"]').text)+'\n')
# #         except:
# #             output_f.write('\n')
#         output_f.write('\n')
#         output_f.flush()
# #         output_f.write(str(driver.find_element_by_css_selector('[class="b_algo"] h2').text)+'\t')
# #         output_f.write(str(driver.find_element_by_css_selector('[class="b_algo"] a').get_attribute('href'))+'\n')
# #         output_f.flush()
#     except Exception as e:
#         output_f.write('\n')
#         output_f.flush()
#         pass

comp = [
"Comprehensive Autism Center - CAC",
"Comprehensive Autism Center - CAC",
"Comprehensive Child Development, Inc.",
"Concord Music",
"Consultant Technologies",
"Contemporary Information Corporation (CIC)",
"Contessa Premium Foods",
"Convaid",
"Cordoba Corporation",
"CoreIP Solutions, Inc.",
"Cosmetic Group USA",
"Country Villa Los Feliz Wellness Centre",
"County of Los Angeles",
"County of Los Angeles Department of Human Resources",
"County of Los Angeles Department of Human Resources",
"COUTS HEATING & COOLING, INC.",
"Covenant House California",
"CPI Solutions",
"Creative Circle",
"Credit.org (Formerly known as Springboard Nonprofit)",
"Crew Knitwear",
"Crews1972",
"Critical Content",
"Crittenton Services #CrittentonHeals",
"Crossroads School for Arts & Sciences",
"Crown Technical Systems",
"Crownco Inc.",
"CSI, Cosmetic Specialties International, LLC",
"CTBC Bank",
"CU Direct",
"Cuba Travel Services",
"Cuba Travel Services",
"Culinary Staffing Service",
"Cumulus Networks",
"Cydcor, Inc.",
"Cypress Creek Renewables",
"DAILYLOOK",
"DAQRI",
"Datron World Communications",
"David & Margaret Youth and Family Services",
"de Toledo High School",
"Deco Lighting",
"Decton Staffing Services",
"deliverLA",
"Della Infotech INC",
"Desert Arc",
"Destiny Home Health & Hospice & Palliative Care",
"Diamond Wipes International",
"Dick Clark Productions",
"Dispensing Dynamics International",
"Diversified Communications HQ",
"DocMagic",
"DOMINOS PIZZA INC",
"DoubleTree by Hilton Los Angeles Downtown",
"Downtown Women's Center",
"DPS Inc.",
"DreamEast Pictures",
"DreamHost",
"Dress The Population",
"DSA Phototech",
"E. S. Kluft & Company, LLC",
"E.V. Roberts",
"Earthbar,LLC",
"East Valley Community Health Center",
"ECA Medical Instruments",
"Echo Advertising",
"ECI",
"Edge Solutions and Consulting Inc.",
"Edjoin.Org",
"EduCare Foundation",
"Edward Thomas Collection",
"eharmony",
"Eisner Pediatric & Family Medical Center",
"ELCO Lighting",
"Electrical Training Institute",
"Electronic Transaction Clearing, Inc.",
"Ellison",
"Encompass Aviation LLC",
"Endologix, Inc.",
"EndPlay, Inc.",
"Enquero",
"ENVi",
"Environmental Charter Schools",
"Eprise",
"EPtronics, Inc.",
"Ergobaby",
"Esperanza Charities DBA Esperanza Services",
"Ettie Lee Youth & Family Services",
"Euro School of Tennis",
"EVELOZCITY",
"Everwell Pasadena",
"EVgo",
"Evolve Treatment Centers",
"EvoNews.com",
"Expression Analysis",
"F&L Galaxy, inc",
"Facility Masters, Inc.",
"Family Service Association",
"Fantasy Activewear, Inc",
"Far East National Bank",
"Far East National Bank",
"Farmer John - Clougherty Packing, LLC",
"Fatburger North America, Inc.",
"Fender Musical Instruments Corporation",
"Fertility & Surgical Associates of California",
"FilmL.A., Inc.",
"Financial Services",
"First Class Vending Inc",
"First Entertainment Credit Union",
"FirstSteps for Kids, Inc.",
"Fitness 19",
"Five Acres--The Boys' and Girls' Aid Society of Los Angeles",
"Five Acres--The Boy's and Girl's Aid Society of Los Angeles",
"Flexogenix",
"FloQast",
"Forest Home",
"Foundation Laboratory",
"FRAME",
"Franklin Loan Center",
"Frasco, Inc.",
"Frasco, Inc.",
"FreedomPop",
"Frieda's Specialty Produce",
"Frimex Hospitality Group",
"Frontier Communities",
"Fruit Growers Supply Company",
"FS Precision Tech",
"FUEL CYCLE",
"Fullscreen",
"FuseFX",
"FuseFX",
"G/M Business Interiors",
"Gamblit Gaming, LLC",
"Gateway Seminary",
"Gateways Hospital and Mental Health Center",
"Gaytan Foods",
"Gaytan Foods",
"GBX Consultants, Inc.",
"Glendora Community Hospital",
"Global Road Entertainment",
"Global Youth Mentorship Initiative",
"Goetzman Group",
"Gold Star Foods",
"Gold Star Foods",
"Golden Road Brewing",
"Golden State Warriors",
"Good Living Services",
"Goodridge Ltd",
"Goodwill Industries of Ventura and Santa Barbara Counties",
"Granada Hills Charter High School",
"Grant & Weber",
"Gravity Brands",
"Greater Hope Foundation",
"Greenland USA",
"Greenspire",
"Greystone Hotels",
"Griffin Capital Company, LLC",
"GroLink Plant Company",
"GSN (Game Show Network)",
"Guitar Center",
"Gumbiner Savett",
"H&M",
"Habitat for Humanity of Greater Los Angeles",
"Hackman Capital Partners & The Culver Studios",
"Hacor Inc.",
"Hal Hays Construction, Inc.",
"Haliburton International Foods, Inc.",
"Hallmark Aviation Services",
"Hallmark Channel",
"Hampton Tedder Electric Co",
"Hangar 24 Craft Brewery",
"Hansen, Jacobson, Teller, Hoberman, Newman, Warren, Richman, Rush & Kaller, LLP",
"Haralambos Beverage Company",
"Haralambos Beverage Company",
"Hardwood Creations, Inc. dba HCI",
"Harley Ellis Devereaux (HED)",
"Harrington Industrial Plastics",
"Harvey Mudd College",
"Haven Health",
"Haven Healthcare",
"Hawker Pacific Aerospace",
"Hawthorne",
"HCI Systems, Inc",
"HeadHunter Group",
"Healthy Smiles for Kids of Orange County",
"HelioPower",
"HemaCare Corporation",
"Hertz Investment Group",
"Hertz Investment Group",
"High Desert Medical Group",
"High Desert Medical Group",
"HigherGround, Inc.",
"Hillsides",
"Hillsides",
"Hilton Los Angeles/Universal City",
"Hilton Los Angeles/Universal City",
"Hispanic Scholarship Fund",
"HMC Architects",
"Holiday Inn Buena Park",
"Hollar",
"Home Instead Senior Care",
"Homeboy Industries",
"Homeless Health Care Los Angeles",
"Hospital Association of Southern California",
"Hospital Association of Southern California",
"Hospitals",
"Hotel Zoso",
"Housing Authority County of San Bernardino",
"Houstons Restaurant",
"Human Rights Watch",
"Human Touch, LLC",
"Hunter Landscape",
"Huntington Health Physicians",
"Huntington Library",
"Hush, Inc",
"Hustler Casino",
"HW Staffing Solutions",
"H-Wave® - Electronic Waveform Lab, Inc.",
"Hyatt Regency Indian Wells Resort & Spa",
"Icon Media Direct",
"Icon Media Direct",
"ID TECH",
"Ignition",
"Impresa Aerospace, LLC.",
"Impresa Aerospace, LLC.",
"Impulse Industries Inc.",
"Individual Foodservice",
"Industrial Electronic Engineers",
"Industrial Tools, Inc.",
"Industrial Valco Inc",
"Ingenium Schools",
"Inizio Interventions, Inc.",
"Inland Empire Job Corps",
"Innovative Dining Group",
"Innovative Micro Technology",
"Insomniac Events",
"Insomniac Events",
"Insomniac Events",
"Integrated Data Services, Inc.",
"Integrated Food Service",
"Integrated Technologies Group, Inc.",
"Intercommunity Child Guidance Center",
"Interface Children & Family Services",
"iPayment, Inc.",
"IR",
"Irvine Scientific",
"J/P Haitian Relief Organization",
"Jack Nadel International",
"Jack Nadel International",
"Jack's Surfboards",
"Jacmar Foodservice Distribution - Southern CA",
"Jakks Pacific",
"Jam City",
"Jam City",
"Jam City",
"James Perse Ent., Inc.",
"Jaya Apparel Group, LLC",
"Jersey Mike's Subs",
"Jet Edge International",
"Jet Sets",
"JFK Memorial Hostipal",
"JMAC Lending",
"Joan's on Third",
"Joni and Friends",
"Joni and Friends",
"JP Allen Inc.",
"JP Allen Inc.",
"JP Allen Inc.",
"JP Allen Inc.",
"JR286",
"JTB USA, Inc.",
"Jukin Media",
"Junior Blind of America",
"JWCH Institute",
"Kappa Alpha Theta Beta Xi Chapter",
"Kate Somerville Skincare, LLC",
"Kayne Anderson Capital Advisors, L.P.",
"KCETLink",
"KCRW",
"Kett Engineering Corporation",
"Kett Engineering Corporation",
"KHEIR Center",
"KHEIR Center",
"King Equipment",
"KitchenSync",
"Klune Industries",
"Koury Engineering",
"Kraco Enterprises, LLC",
"Kravitz, Inc.",
"Kretek International, Inc.",
"Kriser's Natural Pet",
"LA Clippers",
"LA County District Attorney",
"LA Galaxy",
"La Puente Valley ROP",
"La Sierra University",
"La Sierra University",
"LA Solar Group",
"Landmark Network",
"Laritech, Inc.",
"Larry Flynt's Lucky Lady Casino",
"Las Virgenes Municipal Water District",
"LATV Network",
"Lawrence Roll Up Doors, Inc.",
"LBS Financial Credit Union",
"LBS Financial Credit Union",
"LD Products, Inc.",
"LECS",
"Lee Kum Kee USA",
"Lee Kum Kee USA",
"Leg Avenue",
"Legacy MSO, Incorporated",
"Legendary Entertainment",
"Legends",
"LIBERTY Dental Plan",
"Lifetouch N.S.S.",
"Lily Jack",
"Lineage Logistics",
"Lip Ink International",
"Lithographix, Inc.",
"Livingston Memorial VNA",
"LoanMart",
"Lollicup USA, Inc.",
"Los Angeles Angels",
"Los Angeles Community Impact",
"Los Angeles County",
"Los Angeles County",
"Los Angeles County Department of Human Resources",
"Los Angeles County Department of Human Resources",
"Los Angeles County Department of Human Resources",
"Los Angeles County Department of Human Resources",
"Los Angeles County Department of Human Resources",
"Los Angeles District Attorney",
"Los Angeles Dodgers",
"Los Angeles Dodgers",
"Los Angeles Homeless Services Authority",
"Los Angeles Homeless Services Authority",
"Los Angeles Kings",
"Los Angeles Kings",
"Los Angeles Lakers",
"Los Angeles Philharmonic",
"Los Angeles Philharmonic",
"Los Angeles Regional Food Bank",
"Los Angeles Unified School District",
"Lottery.com (AutoLotto, Inc.)",
"Lotus Innovations, LLC",
"Loyola High School",
"Loyola Law School, Los Angeles",
"LT Foods Americas",
"Magic Jump Rentals, Inc.",
"Magna Home Health Care, Inc.",
"Main Street Fibers, Inc.",
"Makeshopncompany, Inc.",
"Managed Resources",
"Managed Resources, Inc",
"Managed Resources, Inc",
"Manhattan Beach Unified School District",
"MANHATTAN MEDIA LLC",
"March Vision Care",
"Marina Landscape, Inc.",
"Marine Corps Logistics Base",
"Mariners Church",
"Markwins Beauty Brands Global",
"Markwins Beauty Brands Global",
"Markwins Beauty Brands Global",
"Marshall Electronics",
"MarVista Entertainment",
"Marymount California University",
"Marymount California University",
"Marymount High School",
"Maternal And Child Health Access",
"MATT Construction Corp.",
"Matthews Real Estate Investment Services",
"Maury Microwave",
"Maxzone Auto Parts Corp.",
"MAYEKAWA USA INC",
"McKinley Children's Center",
"McKinley Children's Center",
"McKinley Children's Center",
"Mckinney Trailer Rentals",
"Mcure Health Solutions",
"Media Services",
"Mediator Law Group",
"Medicus Research",
"Menorah Housing Foundation",
"Mental Health Facility",
"Mercedes Diaz Homes Network",
"Mercedes-Benz Research & Development North America, Inc.",
"MetroSwitch Technologies, Inc.",
"Michael Brandman Associates",
"Michael Stars",
"Midnight Oil",
"Millennium Space Systems",
"Millennium Space Systems",
"Miller Castings, Inc.",
"Miniso",
"Miracle Springs Resort & Spa and Desert Hot Springs Spa Hotel",
"Miramax",
"Mission City Community Network, Inc.",
"Mission Community Hospital",
"Mission Community Hospital",
"Mission Produce Inc.",
"Mob Scene",
"mobileforming",
"mobileforming",
"MobilityWare",
"MOLDEX- METRIC",
"Momentous Insurance Brokerage, Inc.",
"MOMENTUM ENTERPRISE INC.",
"MONOGRAM AEROSPACE FASTENERS",
"MONOGRAM AEROSPACE FASTENERS",
"Monrovia Unified School District",
"Montclair Hospital Medical Center",
"Monte Nido & Affiliates",
"Montebello Unified School Dst",
"Monterey Energy, Inc.",
"Moreno Valley College",
"Moss & Company Property Management",
"Mount Saint Mary's University",
"Mount Saint Mary's University",
"Mr. Stax Inc",
"MSA Consulting, Inc.",
"Mt Baldy Resort",
"MTA DISTRIBUTING",
"MULTICULTURAL LEARNING CENTER",
"Munchkin",
"Murrieta Hot Springs Christian Conference Center",
"MusclePharm, Corporation",
"Music Reports, Inc",
"Musicians Institute",
"Mutual Trading Co., Inc.",
"Naito Corp",
"NAS Insurance Services",
"National Community Renaissance",
"National Community Renaissance",
"Nativo Inc",
"Natren, Inc.",
"Natural History Museum of Los Angeles County",
"Naval Air Station North Island",
"NEC Energy Solutions",
"Neil Capital",
"NEOGOV",
"NetFortris",
"New Designs Charter Schools",
"New Directions for Veterans",
"New Horizons",
"New Horizons SFVAR",
"New World Medical",
"Newhall School District",
"NewMark Merrill Companies",
"Nexus Energy Systems",
"NHN Global",
"Nickelodeon",
"Nissin corporation",
"Noblehouse",
"Nomad Editing Company, Inc",
"NONGSHIM AMERICA, INC.",
"NONGSHIM AMERICA, INC.",
"NONGSHIM AMERICA, INC.",
"Norco College",
"North Hawaii Community Hospital",
"North Orange County Regional Occupational Program",
"Northeast Community Clinics",
"Northrop Grumman",
"Northrop Grumman",
"NRI Distribution Inc",
"NRI Distribution Inc",
"Nutrition Express",
"Occidental College",
"O'Gara Coach Company",
"OmniUpdate",
"OneLegacy",
"On-Site Health & Safety",
"Ontic",
"Operam, Inc.",
"Operation HOPE, Inc.",
"Optimist Youth Homes and Family Services",
"ORCO Block & Hardscape",
"Otto International Inc",
"Otto International, Inc.",
"OWN: The Oprah Winfrey Network",
"Oxford Preparatory Academy",
"Oxgord, Art naturals, Pharmedoc, Stanzino, Truly Commerce, and Day to Day Imports",
"Pacific Advisors",
"Pacific American Fish Co.",
"Pacific Asian Consortium in Employment (PACE)",
"Pacific Coast Tree Experts",
"Pacific Compensation Insurance Company",
"Pacific Dermatology Institute",
"Pacific HealthWorks, LLC",
"Pacific Palisades Charter High School",
"Pacific Palms Resort",
"PACIFIC TRANSFORMER CORPORATION",
"Pacifica Trucks, LLC",
"PADI",
"Paligroup Management LLC",
"Palm Springs Unified School District",
"Palmdale Water District",
"Palo Verde Hospital",
"Palos Verdes Golf Club",
"Palos Verdes Library District",
"Paper Mart",
"Para Los Niños",
"Paradigm Talent Agency",
"Paradigm Talent Agency",
"Paradigm Talent Agency",
"Paragon Laboratories",
"Parking company of America Airports",
"Parsec Inc",
"Partners Advantage Insurance Services, LLC",
"Partners In Leadership",
"Pasadena Humane Society & SPCA",
"Pasadena Unified School District",
"Pasadena Unified School District",
"Pasadena Unified School District",
"Pasadena Unified School District",
"Passages Addiction Treatment Centers",
"Passages Addiction Treatment Centers",
"Passages Addiction Treatment Centers",
"Pathways Management Group",
"Pathways Management Group- Options for Youth Public Charter Schools",
"Paulson Manufacturing Corporation",
"Paya.com",
"Payment Express",
"PCF Restaurant Management",
"PCH Treatment Center",
"PCH Treatment Center",
"Pediatric Therapy Network",
"People Assisting The Homeless (PATH)",
"Performance Designed Products LLC",
"Performance Machine",
"PETROL Advertising",
"Philllips Industries",
"PHYSICAL OPTICS CORPORATION",
"Pinnacle Communication Services",
"Pinnpack Packaging, LLC.",
"Pixi Inc.",
"PK Mechanical Systems Inc",
"PKL Services",
"Plan Check Kitchen + Bar",
"PLAN DO SEE AMERICA",
"Planned Parenthood California Central Coast",
"Planned Parenthood Los Angeles",
"Planned Parenthood Los Angeles",
"Platinum Equity",
"Platt College",
"PneuDraulics, Inc.",
"Polaris Anaheim - Taylor Dunn",
"Pomona College",
"popchips",
"Port of Long Beach",
"Port of Long Beach",
"Port Plastics",
"Premier America Credit Union",
"Premier America Credit Union",
"Premier Healthcare Services",
"Premier Mounts",
"Price Transfer",
"PRIDE INTERMODAL INC",
"Prime MSO",
"Prime Wire & Cable, Inc.",
"Prime-Line Products",
"Principia College",
"PRN Ambulance, Inc.",
"Progressive Produce",
"Project Return Peer Support Network",
"Prominence Treatment Center",
"Promote",
"Proper Hospitality",
"PROPERTY MANAGEMENT",
"Prosum",
"Prudential Lighting Corporation",
"PS Business Parks, Inc.",
"PSC Biotech",
"PTI Technologies",
"PureTek",
"Purosil",
"QAI Laboratories",
"Quality Driver Solutions, Inc.",
"Quality Innovative Solutions, Inc.",
"Quandary Construction",
"Quik pick Express",
"Quik Pick Express, LLC",
"QuinStar Technology Inc.",
"Radiology Partners",
"Rainbo Records",
"Rancho California Water District",
"Rancho Pacific Electric Inc.",
"Rancho Physical Therapy",
"Razor USA LLC",
"REACH - Resource for Education, Advocacy, Communication, and Housing",
"REAL Journey Academies",
"RealtyMogul.com",
"Reborn Cabinets",
"RECON Engineering & Construction",
"Redbarn Pet Products",
"Redlands Conservatory of Music",
"REEVE STORE EQUIPMENT CO.",
"Regent, L.P.",
"Reliable Energy Management, Inc.",
"Rescue Mission Alliance",
"Resolute Transportation, Inc",
"Revival LA",
"Rexford Industrial",
"Right At Home",
"Rincon Consultants, Inc.",
"Rios Clementi Hale Studios",
"RJT Compuquest, Inc.",
"RJT Solution Beacon",
"RMA Group, Inc.",
"RNG Group Inc. dba Renogy Solar",
"Robbins Brothers",
"Robbins Brothers, The Engagement Ring Store",
"Robin's Jean",
"Robin's Jean",
"Rock-It Cargo USA LLC",
"Rock-It Cargo USA LLC",
"Rockview Farms",
"Rogers & Cowan",
"Roll-A-Shade",
"Rolling Hills Country Club - Rolling Hills Estates, California",
"Rolling Hills Covenant Church",
"Romeo Power Technology",
"Ronpak, Inc.",
"Roundabout Theatre Company",
"RPS",
"RSA Engineered Products, LLC.-",
"RSA Films Inc.",
"RTI Properties",
"RTS Solutionz",
"Ruhnau Clarke Architects",
"Ruhnau Ruhnau Clarke Architects Planners",
"Russ Bassett Corporation",
"RWC - Boerner Truck Center",
"Saalex Solutions",
"Saalex Solutions, Inc.",
"Saatchi & Saatchi (We Are Saatchi)",
"Saban Community Clinic",
"Saban Community Clinic",
"Saban Community Clinic",
"Saddleback Church",
"SAG-Producers Pension Plan",
"SalonCentric - A Subsidiary of L'Oreal USA",
"San Bernardino County",
"San Diego State University",
"San Fernando Valley Community Mental Health Center",
"San Fernando Valley Community Mental Health Center",
"Sandals Church",
"Sanders & Wohrman Corporation",
"SCE Federal Credit Union",
"Scenario",
"Science 37",
"Scosche Industries, Inc.",
"Sears Holdings Corporation",
"SecurCare Self Storage",
"Securitas Security Services USA, Inc.",
"SEIU Local 2015",
"SEIU Local 2015",
"Self Esteem - All Access Apparel Inc",
"Self-Employed",
"Senturion",
"ServiceMesh, Inc.",
"Servpro Of Encino",
"Shepard Bros., Inc.",
"Sherman Oaks Hospital",
"Sherman Oaks Hospital",
"Shield HealthCare - Medical Supplies for Care at Home Since 1957",
"Shields for Families",
"Sierra Aluminum Company",
"Sign Spinner Advertising (Sign Spinner Ads)",
"SingerLewak LLP",
"Sit 'n Sleep",
"SJ Distributors Inc.",
"Skid Row Housing Trust",
"Skilled Nursing Pharmacy",
"Sky Zone Franchise Group",
"Skydance",
"SmartyPants Vitamins",
"Smashbox Cosmetics",
"SMG",
"SnackNation",
"SnF Management Company",
"Soba Recovery Center",
"Sober College",
"Soboba Band of Luiseno Indians",
"Soboba Band of Luiseño Indians",
"SolarMax Technology",
"SolarReserve",
"Soledad Enrichment Action",
"Solex Contracting",
"Solugenix",
"sonnen",
"SonoSim, Inc.",
"South Bay Family Health Care",
"South Bay Family Health Care",
"South Coast Winery & Spa",
"Southern California Association of Governments",
"Southern California Association of Governments",
"Southern California Association of Governments",
"Southwest ToyotaLift (Southwest Material Handling, Inc.)",
"Spa Resort Casino",
"Spatz Laboratories",
"Spectrolab",
"Spectrum A Repligen Brand",
"Spencer Gold",
"Spicers Paper, Member of Central National-Gottesman Inc.",
"Spokeo",
"Spyder Auto",
"SRO Housing Corporation",
"SRO Housing Corporation",
"St. Baldrick's Foundation",
"St. John of God Retirement and Care Center",
"St. Mary Medical Center",
"StemCyte Cord Blood Bank",
"Sterling Pacific Meat Co.",
"Stila Cosmetics",
"Stoopid Buddy Stoodios",
"STX Entertainment",
"STX Entertainment",
"STX Entertainment",
"Summit Interconnect",
"Sun Air Jets",
"Sun Noodle",
"Sunkist Growers",
"SunLine Transit Agency",
"Sunrider International",
"SuperCare Health",
"SuperInterns.com",
"Superior Communications",
"Superior Duct Fabrication Inc",
"Superior Electrical Mechanical and Plumbing",
"Survival Insurance Brokerage",
"Suttles Plumbing and Mechanical Corp",
"Swami International",
"T and D Communications, Inc.",
"T. Marzetti Company",
"Tacori",
"TAIT & Associates, Inc",
"Tanner LLC",
"Taylored Services, LLC",
"Teacher Created Materials",
"Team Rubicon USA",
"Teledyne Scientific & Imaging",
"Tennis Channel",
"Tesloop",
"The Accelerated Schools: ACES, TAS & WAHS",
"The American Film Institute",
"The Annenberg Foundation Trust at Sunnylands",
"The Annenberg Foundation Trust at Sunnylands",
"The Archer School for Girls",
"The Bella Vita, A Beautiful Life Psychology Group",
"The Borgen Project",
"The Borgen Project",
"The Chicago School of Professional Psychology",
"The Chicago School of Professional Psychology",
"The Children's Clinic, \"Serving Children and Their Families\"",
"The Children's Clinic, \"Serving Children and Their Families\"​",
"The Conga Room",
"The Designory",
"The Doctor's Choice Home Health Agency",
"The Famous Group",
"The Gill Corporation",
"The Guidance Center, Long Beach",
"The Hollywood Roosevelt",
"The Holman Group",
"The Home Depot",
"The Honest Company",
"The Honest Company",
"The Hundreds",
"The Langham Hotels and Resorts",
"The Liberty Company Insurance Brokers",
"The Madera Group",
"The Oncology Institute of Hope and Innovation",
"The Oncology Institute of Hope and Innovation",
"The Oncology Institute of Hope and Innovation",
"The Refinery Creative",
"The Refinery Creative",
"The Sheraton Pasadena Hotel",
"The Skirball Cultural Center",
"The Sliding Door Company",
"THE VILLA TREATMENT CENTER LLC",
"The World Protection Group",
"Think Insurance & Financial Services, LLC",
"Think Together",
"Tierra del Sol Foundation",
"Tinder, Inc.",
"Titan Construction & Solar",
"TMT Communications, Inc.",
"Tofasco of America Inc.",
"Tool of North America",
"Topson Downs of California, Inc.",
"Topson Downs of California, Inc.",
"Topson Downs of California, Inc.",
"Topson Downs of California, Inc.",
"TOTAL TRANSPORTATION SERVICES INC.",
"Totally Kids Rehabilitation Hospital",
"Totally Kids Rehabilitation Hospital",
"Tours4Fun",
"Tower Energy Group",
"Traffic Solutions Corporation",
"Transamerica Financial Advisors, Inc.",
"Transtech Engineers, Inc.",
"Treeium Inc.",
"TrellisWare Technologies",
"Trend Technologies",
"Tri City Mental Health Services",
"Tridien Medical",
"Trilogy Plumbing Incorporated",
"TriMed",
"Tri-Signal Integration, Inc",
"Trivec Avant Corporation",
"TruConnect",
"Turelk, Inc.",
"TVG Network & Betfair US",
"TWIW, Tolman and Wiker Insurance",
"TWS Facility Services",
"U.S. Army Reserve",
"UC San Diego Computer Sciences and Engineering",
"UCLA Extension",
"UCLA Radio",
"UCSD Department of Cellular and Molecular Medicine",
"Unilever",
"Union Rescue Mission - Los Angeles",
"Union Station Homeless Services",
"United Pacific Industries, Inc.",
"United Service Technologies, Inc.",
"United Staffing Solutions, Inc. (USSI)",
"United States Air Force",
"United States Army Human Resources Command",
"United States Army Reserve",
"United Talent Agency",
"United Talent Agency",
"Universal Bank",
"Update Legal",
"UPS",
"UPS",
"Urbane Cafe",
"URO Parts / A.P.A. Industries, Inc.",
"Urth Caffe",
"US Army",
"Us Army Reserves",
"USC Suzanne Dworak-Peck School of Social Work",
"Used Cardboard Boxes, Inc.",
"Utility Design Services Inc.",
"VA Hospital",
"VACCO Industries",
"Valet Parking Service",
"VALLARTA SUPERMARKETS, VSI",
"Valley Community Healthcare",
"Valley Power Systems",
"Valley Power Systems",
"Valley Power Systems",
"Vavrinek, Trine, Day & Co., LLP",
"Vavrinek, Trine, Day & Co., LLP",
"VectorUSA",
"Veg-Fresh Farms",
"Vendor Direct Solutions",
"Vendor Direct Solutions",
"Ventura Coastal, LLC",
"Verliance Inc.",
"Versa Products, Inc",
"Viele and Sons",
"Viewpoint School",
"Villa Park Trucking Inc",
"Vince",
"Vinyl Technology, Inc.",
"Violence Intervention Program",
"Virtual Enterprises International, Inc. - DARREL",
"Virtuoso Medical Management",
"Visions Adolescent Treatment Centers",
"Visiting Angels Glendora",
"Vista Investments, LLC",
"Vista Investments, LLC",
"Vistamar School",
"Volutone",
"Wag Labs Inc.",
"Wagstaff Worldwide",
"Waldorf Astoria Beverly Hills",
"Waldorf Astoria Beverly Hills",
"Waldorf Astoria Beverly Hills",
"Water and Power Community Credit Union",
"WCCT Global",
"We Care Plumbing Heating Air and Solar",
"Weber Logistics",
"WePackItAll",
"West Anaheim Medical Center",
"West Coast Aerospace",
"West Coast Aviation Services",
"Western General Insurance",
"Western General Insurance Company",
"Western Municipal Water District",
"Westin Bonaventure",
"Westland Floral Company",
"Westland Floral Company",
"Westport Properties, Inc",
"Westside Regional Center",
"WFG Lender Services, LLC",
"WG&S LLP",
"Whittier College",
"Whittier College",
"Wilbur Curtis",
"William Warren Group",
"Wilson Creek Winery",
"Wirelessbro Inc",
"WISE & Healthy Aging",
"WLCAC",
"WorkCare, Inc.",
"Working With Autism",
"WORLD CLASS DISTRIBUTION, INC.",
"Worldwide Facilities, LLC",
"Worthe Real Estate Group",
"Writers Guild of America West",
"Xceed Financial Credit Union",
"Xencor",
"Xprite USA",
"Xprize",
"Yinlun TDI",
"YONEKYU CORPORATION",
"Your Snack Innovation Partner - Private Label and Branded Snacks",
"Youth Policy Institute",
"Youth Policy Institute",
"YouthBuild Charter School of California",
"ZAG.com",
"ZEFR, Inc.",
"Zelox",
"Zodiac Inflight Innovations",
"Zoic Studios",
"ZPower",
"Zuber Lawler & Del Duca",
]

driver.get('https://www.google.com/search?source=hp&ei=L9drW6TYCtSb9QPJtq2gCg&q=a&oq=a&gs_l=psy-ab.3..35i39k1l2j0i131i67k1j0i131k1l2j0j0i131k1j0l2j0i131k1.2011.2011.0.2650.2.1.0.0.0.0.170.170.0j1.1.0....0...1c.1.64.psy-ab..1.1.168.0...0.laqwNZZ6y_Y')
for c in comp:
    #print (c)
    try:
        driver.find_element_by_css_selector('[id="lst-ib"]').clear()
        driver.find_element_by_css_selector('[id="lst-ib"]').send_keys(c)
        driver.find_element_by_css_selector('[id="lst-ib"]').send_keys(Keys.ENTER)
        time.sleep(3)
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="s"] cite')))
        a = driver.find_element_by_css_selector('[class="s"] cite').text
        print (c+'\t'+a)
        
    except Exception as e:
        print (c)
        