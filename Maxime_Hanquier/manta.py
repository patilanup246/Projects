'''
Created on Jun 15, 2017

@author: Mukadam
'''
from pyquery import PyQuery
import math
import webbrowser
import time

#file_in = open('C:\\Users\\Mukadam\\Downloads\\file.txt','r').read()

#pq = PyQuery(file_in)

dict_links = [{"value":90.00,"link":"/world/Europe/United+Kingdom/abrasive_products--E8123/"},
{"value":946.00,"link":"/world/Europe/United+Kingdom/adhesives_and_sealants--E837B/"},
{"value":3.00,"link":"/world/Europe/United+Kingdom/alkalies_and_chlorine--E832C/"},
{"value":26.00,"link":"/world/Europe/United+Kingdom/aluminum_die_castings--E816B/"},
{"value":9.00,"link":"/world/Europe/United+Kingdom/aluminum_extruded_products--E8162/"},
{"value":7.00,"link":"/world/Europe/United+Kingdom/aluminum_rolling_and_drawing_nec--E8163/"},
{"value":6.00,"link":"/world/Europe/United+Kingdom/aluminum_sheet_plate_and_foil--E8161/"},
{"value":10.00,"link":"/world/Europe/United+Kingdom/asbestos_products--E8124/"},
{"value":17.00,"link":"/world/Europe/United+Kingdom/asphalt_felts_and_coatings--E83B8/"},
{"value":23.00,"link":"/world/Europe/United+Kingdom/asphalt_paving_mixtures_and_blocks--E83B7/"},
{"value":24.00,"link":"/world/Europe/United+Kingdom/automatic_controls_for_regulating_residential_and_commercial_environments_and_appliances--E833Y/"},
{"value":15.00,"link":"/world/Europe/United+Kingdom/biological_products_except_diagnostic_substances--E8344/"},
{"value":14.00,"link":"/world/Europe/United+Kingdom/boot_and_shoe_cut_stock_and_findings--E8083/"},
{"value":879.00,"link":"/world/Europe/United+Kingdom/brick_and_structural_clay_tile--E80FB/"},
{"value":13.00,"link":"/world/Europe/United+Kingdom/carbon_and_graphite_products--E8270/"},
{"value":9.00,"link":"/world/Europe/United+Kingdom/carbon_black--E837F/"},
{"value":4.00,"link":"/world/Europe/United+Kingdom/cellulosic_manmade_fibers--E8337/"},
{"value":54.00,"link":"/world/Europe/United+Kingdom/cement_hydraulic--E80F1/"},
{"value":93.00,"link":"/world/Europe/United+Kingdom/ceramic_wall_and_floor_tile--E80FD/"},
{"value":1151.00,"link":"/world/Europe/United+Kingdom/chemicals_and_allied_products_nec--E80A9/"},
{"value":746.00,"link":"/world/Europe/United+Kingdom/chemicals_and_chemical_preparations_nec--E8383/"},
{"value":19.00,"link":"/world/Europe/United+Kingdom/clay_refractories--E80FF/"},
{"value":1133.00,"link":"/world/Europe/United+Kingdom/coal_and_other_minerals_and_ores--E803Y/"},
{"value":746.00,"link":"/world/Europe/United+Kingdom/concrete_block_and_brick--E810F/"},
{"value":191.00,"link":"/world/Europe/United+Kingdom/concrete_products_except_block_and_brick--E8110/"},
{"value":381.00,"link":"/world/Europe/United+Kingdom/converted_paper_and_paperboard_products_nec--E82A7/"},
{"value":104.00,"link":"/world/Europe/United+Kingdom/corrugated_and_solid_fiber_boxes--E828D/"},
{"value":499.00,"link":"/world/Europe/United+Kingdom/cut_stone_and_stone_products--E8119/"},
{"value":4.00,"link":"/world/Europe/United+Kingdom/cyclic_organic_crudes_and_intermediates_and_organic_dyes_and_pigments--E8361/"},
{"value":143.00,"link":"/world/Europe/United+Kingdom/die_cut_paper_and_paperboard_and_cardboard--E82A3/"},
{"value":399.00,"link":"/world/Europe/United+Kingdom/drawing_and_insulating_of_nonferrous_wire--E8165/"},
{"value":33.00,"link":"/world/Europe/United+Kingdom/explosives--E837C/"},
{"value":1930.00,"link":"/world/Europe/United+Kingdom/fabricated_rubber_products_nec--E8045/"},
{"value":11.00,"link":"/world/Europe/United+Kingdom/fertilizers_mixing_only--E836B/"},
{"value":3.00,"link":"/world/Europe/United+Kingdom/fiber_cans_tubes_drums_and_similar_products--E828F/"},
{"value":155.00,"link":"/world/Europe/United+Kingdom/flat_glass--E80D3/"},
{"value":281.00,"link":"/world/Europe/United+Kingdom/folding_paperboard_boxes_including_sanitary--E8291/"},
{"value":45.00,"link":"/world/Europe/United+Kingdom/gaskets_packing_and_sealing_devices--E8035/"},
{"value":22.00,"link":"/world/Europe/United+Kingdom/gum_and_wood_chemicals--E835D/"},
{"value":61.00,"link":"/world/Europe/United+Kingdom/gypsum_products--E8113/"},
{"value":92.00,"link":"/world/Europe/United+Kingdom/industrial_gases--E832D/"},
{"value":173.00,"link":"/world/Europe/United+Kingdom/industrial_inorganic_chemicals_nec--E8333/"},
{"value":67.00,"link":"/world/Europe/United+Kingdom/industrial_organic_chemicals_nec--E8365/"},
{"value":36.00,"link":"/world/Europe/United+Kingdom/inorganic_pigments--E8330/"},
{"value":73.00,"link":"/world/Europe/United+Kingdom/leather_tanning_and_finishing--E806F/"},
{"value":15.00,"link":"/world/Europe/United+Kingdom/lime--E8112/"},
{"value":14.00,"link":"/world/Europe/United+Kingdom/lubricating_oils_and_greases--E83E0/"},
{"value":40.00,"link":"/world/Europe/United+Kingdom/manmade_organic_fibers_except_cellulosic--E8338/"},
{"value":1428.00,"link":"/world/Europe/United+Kingdom/metals_service_centers_and_offices--E8033/"},
{"value":1.00,"link":"/world/Europe/United+Kingdom/mineral_wool--E8128/"},
{"value":4.00,"link":"/world/Europe/United+Kingdom/minerals_and_earths_ground_or_otherwise_treated--E8127/"},
{"value":108.00,"link":"/world/Europe/United+Kingdom/nitrogenous_fertilizers--E8369/"},
{"value":5.00,"link":"/world/Europe/United+Kingdom/nonclay_refractories--E8129/"},
{"value":454.00,"link":"/world/Europe/United+Kingdom/nonmetallic_mineral_products_nec--E812B/"},
{"value":273.00,"link":"/world/Europe/United+Kingdom/paint_varnishes_and_supplies--E80C6/"},
{"value":412.00,"link":"/world/Europe/United+Kingdom/paints_varnishes_lacquers_enamels_and_allied_products--E8353/"},
{"value":61.00,"link":"/world/Europe/United+Kingdom/pesticides_and_agricultural_chemicals_nec--E836F/"},
{"value":50.00,"link":"/world/Europe/United+Kingdom/petroleum_refining--E838F/"},
{"value":1.00,"link":"/world/Europe/United+Kingdom/phosphatic_fertilizers--E836A/"},
{"value":556.00,"link":"/world/Europe/United+Kingdom/plastics_material_and_synthetic_resins_and_nonvulcanizable_elastomers--E8335/"},
{"value":2905.00,"link":"/world/Europe/United+Kingdom/plastics_products_nec--E8059/"},
{"value":16.00,"link":"/world/Europe/United+Kingdom/plastics_foil_and_coated_paper_bags--E82A1/"},
{"value":245.00,"link":"/world/Europe/United+Kingdom/primary_production_of_aluminum--E814E/"},
{"value":17.00,"link":"/world/Europe/United+Kingdom/primary_smelting_and_refining_of_copper--E814B/"},
{"value":150.00,"link":"/world/Europe/United+Kingdom/primary_smelting_and_refining_of_nonferrous_metals_except_copper_and_aluminum--E8153/"},
{"value":40.00,"link":"/world/Europe/United+Kingdom/printing_ink--E837D/"},
{"value":370.00,"link":"/world/Europe/United+Kingdom/products_of_petroleum_and_coal_nec--E83E7/"},
{"value":726.00,"link":"/world/Europe/United+Kingdom/ready_mixed_concrete--E8111/"},
{"value":7.00,"link":"/world/Europe/United+Kingdom/rolling_drawing_and_extruding_of_copper--E815F/"},
{"value":12.00,"link":"/world/Europe/United+Kingdom/rolling_drawing_and_extruding_of_nonferrous_metals_except_copper_and_aluminum--E8164/"},
{"value":20.00,"link":"/world/Europe/United+Kingdom/rubber_and_plastics_footwear--E8015/"},
{"value":11.00,"link":"/world/Europe/United+Kingdom/rubber_and_plastics_hose_and_belting--E803X/"},
{"value":572.00,"link":"/world/Europe/United+Kingdom/sanitary_food_containers_except_folding--E8290/"},
{"value":132.00,"link":"/world/Europe/United+Kingdom/sanitary_paper_products--E82A4/"},
{"value":37.00,"link":"/world/Europe/United+Kingdom/secondary_smelting_and_refining_of_nonferrous_metals--E8155/"},
{"value":3.00,"link":"/world/Europe/United+Kingdom/setup_paperboard_boxes--E828C/"},
{"value":61.00,"link":"/world/Europe/United+Kingdom/soaps_and_other_detergents_except_speciality_cleaners--E8349/"},
{"value":45.00,"link":"/world/Europe/United+Kingdom/speciality_cleaning_polishing_and_sanitary_preparations--E834A/"},
{"value":268.00,"link":"/world/Europe/United+Kingdom/steel_pipe_and_tubes--E813D/"},
{"value":14.00,"link":"/world/Europe/United+Kingdom/structural_clay_products_nec--E8103/"},
{"value":6.00,"link":"/world/Europe/United+Kingdom/surface_active_agents_finishing_agents_sulfonated_oils_and_assistants--E834B/"},
{"value":23.00,"link":"/world/Europe/United+Kingdom/synthetic_rubber--E833X/"},
{"value":59.00,"link":"/world/Europe/United+Kingdom/tires_and_inner_tubes--E800B/"},
{"value":736.00,"link":"/world/Europe/United+Kingdom/-/London/materials_chemicals--E8/"},
{"value":354.00,"link":"/world/Europe/United+Kingdom/-/Manchester/materials_chemicals--E8/"},
{"value":278.00,"link":"/world/Europe/United+Kingdom/-/Glasgow/materials_chemicals--E8/"},
{"value":257.00,"link":"/world/Europe/United+Kingdom/-/Bristol/materials_chemicals--E8/"},
{"value":243.00,"link":"/world/Europe/United+Kingdom/-/Sheffield/materials_chemicals--E8/"},
{"value":228.00,"link":"/world/Europe/United+Kingdom/-/Leicester/materials_chemicals--E8/"},
{"value":221.00,"link":"/world/Europe/United+Kingdom/-/Leeds/materials_chemicals--E8/"},
{"value":212.00,"link":"/world/Europe/United+Kingdom/-/Nottingham/materials_chemicals--E8/"},
{"value":168.00,"link":"/world/Europe/United+Kingdom/-/Stoke-On-Trent/materials_chemicals--E8/"},
{"value":152.00,"link":"/world/Europe/United+Kingdom/-/Liverpool/materials_chemicals--E8/"},
{"value":136.00,"link":"/world/Europe/United+Kingdom/-/Bradford/materials_chemicals--E8/"},
{"value":135.00,"link":"/world/Europe/United+Kingdom/-/Belfast/materials_chemicals--E8/"},
{"value":131.00,"link":"/world/Europe/United+Kingdom/-/Norwich/materials_chemicals--E8/"},
{"value":128.00,"link":"/world/Europe/United+Kingdom/-/Southampton/materials_chemicals--E8/"},
{"value":121.00,"link":"/world/Europe/United+Kingdom/-/Aberdeen/materials_chemicals--E8/"},
{"value":117.00,"link":"/world/Europe/United+Kingdom/-/Chesterfield/materials_chemicals--E8/"},
{"value":117.00,"link":"/world/Europe/United+Kingdom/-/Newport/materials_chemicals--E8/"},
{"value":116.00,"link":"/world/Europe/United+Kingdom/-/Coventry/materials_chemicals--E8/"},
{"value":112.00,"link":"/world/Europe/United+Kingdom/-/Hull/materials_chemicals--E8/"},
{"value":111.00,"link":"/world/Europe/United+Kingdom/-/Bolton/materials_chemicals--E8/"}]

#webbrowser.open('https://www.manta.com')

total = 1   
print 'start'
for a in dict_links:
    for i in range(1, int( math.ceil(   a['value']/35   ) ) +1 ):
        print 'https://www.manta.com'+a['link']+'?pg='+str(i)
#         webbrowser.open('https://www.manta.com'+a['link']+'?pg='+str(i))
#         if (total%2) == 0:
#             time.sleep(5)
        total+=1
    
    