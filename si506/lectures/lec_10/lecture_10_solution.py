# SI 506: Lecture 10

import pprint

# Instantiate a custom PrettyPrinter object
pp = pprint.PrettyPrinter(indent=1, width=100, compact=True)

# Includes faux test record (id=999999)
station_data = [
    ['id', 'station_name', 'facility_type', 'access_code', 'access_days_time', 'restricted_access', 'city', 'zip', 'street_address', 'intersection_directions', 'ev_network', 'ev_connector_types', 'ev_dc_fast_num', 'ev_level1_evse_num', 'ev_level2_evse_num', 'ev_other_evse', 'ev_pricing', 'date_last_confirmed'],
    ['41828', 'DTE Energy - Ann Arbor Ashley Mews Building', 'UTILITY', 'private', 'Employee and official visitor use only, 24 hours daily with employee security badge', None, 'Ann Arbor', '48104', '414 S Main St', 'Southeast corner of W Williams Street and S Ashley Street; in underground parking garage, entrance off of S Ashley Street; visitor parking spaces #1 and #2.', 'Non-Networked', 'J1772', None, None, '1', None, None, '2020-10-09'],
    ['42726', 'Ann Arbor Downtown Development Authority - Library Parking Structure', 'LIBRARY', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '319 S Fifth Ave', 'Sift between Liberty and William', 'Non-Networked', 'J1772', None, None, '9', None, 'Variable parking fee', '2021-07-14'],
    ['44282', 'Ann Arbor Downtown Development Authority - Ann Ashley Parking Structure', 'PARKING_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '120 W Ann St', 'Ann and Ashley', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44283', 'Ann Arbor Downtown Development Authority - Catherine and Fourth Surface Lot', 'PARKING_LOT', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '121 Catherine St', 'Catherine and Fourth', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44284', 'Ann Arbor Downtown Development Authority - Forrest Parking Structure', 'PARKING_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '650 Forrest St', 'Forrest and S University', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44285', 'Ann Arbor Downtown Development Authority - Maynard Parking Structure', 'PARKING_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '316 Maynard St', 'Maynard between Liberty and William', 'Non-Networked', 'J1772', None, None, '4', None, 'Variable parking fee', '2021-07-14'],
    ['44286', 'Ann Arbor Downtown Development Authority - William Street Parking Structure', 'PARKING_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '115 William St', 'William and Main', 'Non-Networked', 'J1772', None, None, '2', None, 'Variable parking fee', '2021-07-14'],
    ['44287', 'Ann Arbor Nissan', 'CAR_DEALER', 'public', 'Dealership business hours', 'False', 'Ann Arbor', '48103', '3975 Jackson Rd', None, 'Non-Networked', 'CHADEMO, J1772, J1772COMBO', '2', None, '1', None, 'Free', '2022-03-07'],
    ['44288', 'Ann Arbor Nissan', 'CAR_DEALER', 'private', None, None, 'Ann Arbor', '48103', '3975 Jackson Rd', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-03-07'],
    ['44773', 'IMRA America', 'OFFICE_BLDG', 'private', 'Employee and fleet use only', None, 'Ann Arbor', '48105', '1044 Woodridge Ave', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-06-14'],
    ['62417', 'U-M ANN ARBOR WALL STREET #2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '1041 Wall St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['63647', 'Varsity Ford', 'CAR_DEALER', 'private', None, None, 'Ann Arbor', '48103', '3480 Jackson Rd', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-06-14'],
    ['74325', 'Ann Arbor Downtown Development Authority - Ashley and Washington Parking Structure', 'PAY_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '215 W Washington', 'Washington and Ashley', 'Non-Networked', 'J1772', None, None, '3', None, 'Variable parking fee', '2022-05-05'],
    ['79282', 'First Martin', 'OFFICE_BLDG', 'private', 'Employee use only', None, 'Ann Arbor', '48104', '115 Depot St', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-09-14'],
    ['80037', 'MEADOWLARK BLDG STATION 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48103', '3250 W Liberty Rd', None, 'ChargePoint Network', 'J1772', None, None, '1', None, None, '2022-09-26'],
    ['99362', 'A & D Technology', 'OFFICE_BLDG', 'public', 'Open to public after company business hours', 'True', 'Ann Arbor', '48108', '4622 Runway Blvd', None, 'Non-Networked', 'J1772', None, None, '4', None, 'Free', '2020-12-03'],
    ['102221', 'Meijer - Tesla Supercharger', None, 'public', '24 hours daily; for Tesla use only', None, 'Ann Arbor', '48103', '3145 Ann Arbor-Saline Road', None, 'Tesla', 'TESLA', '8', None, None, None, '$0.28 per kWh; $0.26 per minute above 60 kW and $0.13 per minute at or below 60 kW', '2021-10-11'],
    ['114460', 'Sheraton Ann Arbor Hotel - Tesla Destination', 'HOTEL', 'public', '24 hours daily; for customer use only; see front desk for access', None, 'Ann Arbor', '48108', '3200 Boardwalk Dr', None, 'Tesla Destination', 'J1772, TESLA', None, None, '4', None, 'Free', '2020-11-03'],
    ['145371', 'Roundtree Place', None, 'public', '24 hours daily', None, 'Ypsilanti', '48197', '2539 Ellsworth Rd', None, 'Electrify America', 'CHADEMO, J1772COMBO', '6', None, None, None, None, '2022-09-07'],
    ['147501', 'MEIJER STORES 064 SALINE RD 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48108', '3145 Ann Arbor-Saline Rd', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['147555', 'U-M ANN ARBOR NCRC STATION 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '2800 Plymouth Rd', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['164341', '173 - Ann Arbor', None, 'public', '24 hours daily', None, 'Ann Arbor', '48103', '5645 Jackson Road', None, 'Greenlots', 'CHADEMO, J1772, J1772COMBO', '2', None, '4', None, None, '2022-09-26'],
    ['168052', 'The Ypsilanti Performance Space', 'OTHER_ENTERTAINMENT', 'public', '24 hours daily', 'False', 'Ypsilanti', '48197', '218 N Adams St', None, 'Non-Networked', 'J1772', None, None, '1', None, '$1 per hour; $5 per day', '2022-08-10'],
    ['168663', 'Car & Driver - Tesla Destination', None, 'public', '24 hours daily; for customer use only; see front desk for access', None, 'Ann Arbor', '48108', '1585 Eisenhower Place', None, 'Tesla Destination', 'TESLA', None, None, '2', None, 'Free', '2020-11-03'],
    ['171786', 'U-M ANN ARBOR WALL STREET #1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '1041 Wall St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['172462', 'MEADOWLARK BLDG STATION 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48103', '3250 W Liberty Rd', None, 'ChargePoint Network', 'J1772', None, None, '1', None, None, '2022-09-26'],
    ['174646', 'MEIJER STORES 064 SALINE RD 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48108', '3145 Ann Arbor-Saline Rd', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['174657', 'U-M ANN ARBOR NCRC STATION 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '2800 Plymouth Rd', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['184715', 'NOAA', 'FED_GOV', 'private', 'Drivers must bring their own J1772 cordset for Level 1 charging', None, 'ANN ARBOR', '48108', '4840 S State Rd', None, 'Non-Networked', 'NEMA515', None, '2', None, None, None, '2021-02-22'],
    ['184845', 'EPA Ann Arbor - Station 1', 'FED_GOV', 'private', None, None, 'Ann Arbor', '48105', '2565 Plymouth Rd', None, 'Non-Networked', 'J1772', None, None, '6', None, None, '2021-02-22'],
    ['184846', 'EPA Ann Arbor - Station 2', 'FED_GOV', 'private', 'Drivers must bring their own J1772 cordset for Level 1 charging', None, 'Ann Arbor', '48105', '2565 Plymouth Rd', None, 'Non-Networked', 'NEMA515', None, '1', None, None, 'Free', '2021-02-22'],
    ['187890', 'HAMPTON -YPSI DTWYP #1', None, 'public', '24 hours daily', None, 'Ypsilanti', '48197', '515 James L Hart Pkwy', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['187922', 'BMW ANN ARBOR STATION 01', None, 'public', '24 hours daily', None, 'Ann Arbor', '48103', '501 Auto Mall Dr', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['188119', 'Prentice Partners', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '830 Henry Street', None, 'Greenlots', 'J1772', None, None, '10', None, None, '2022-09-26'],
    ['198009', 'Hover + Greene', 'MULTI_UNIT_DWELLING', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '950 Greene St', None, 'EV Connect', 'J1772', None, None, '4', None, None, '2021-11-04'],
    ['198073', 'BEEKMAN STATION 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '1200 Broadway St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['199100', 'FLEET SERVICES DCFC-STATION 4', None, 'public', '24 hours daily', None, 'Ann Arbor, MI', '48104', '301 E. Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['199101', 'FLEET SERVICES DCFC-STATION 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '301 E. Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['199102', 'FLEET SERVICES DCFC-STATION 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '301 E Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['200995', 'FLEET SERVICES DCFC-STATION 3', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '301 E Huron St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['201411', 'U-M ANN ARBOR ANN 1 & 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '1115 E Ann St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['201412', 'U-M ANN ARBOR ANN 3', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '1101-1189 E Ann St', None, 'ChargePoint Network', 'J1772', None, None, '1', None, None, '2022-09-26'],
    ['201416', 'U-M ANN ARBOR SC32', None, 'public', '24 hours daily', None, 'Ann Arbor', '48109', '1024 Greene St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['201417', 'U-M ANN ARBOR NC27 1 & 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48109', '1300 Murfin Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['202411', 'WASHTENAW BP 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48108', '4975 Washtenaw Ave', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['202417', 'WASHTENAW BP 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48108', '4975 Washtenaw Ave', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['216275', 'Suburban Chevrolet', 'CAR_DEALER', 'public', '24 hours daily', 'False', 'Ann Arbor', '48103', '3515 Jackson Rd', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['216276', 'Fourth & Washington Parking Garage', 'PARKING_GARAGE', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '123 E Washington St', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['216277', 'Audi Ann Arbor', 'CAR_DEALER', 'public', '24 hours daily', 'False', 'Ann Arbor', '48104', '2575 S State St', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['216278', 'ProQuest Employee Parking Garage', 'PARKING_GARAGE', 'private', '24 hours daily', None, 'Ann Arbor', '48108', '789 E Eisenhower Pkwy', None, 'Non-Networked', 'J1772', None, None, '4', None, None, '2022-05-05'],
    ['216279', 'Staybridge Suites', 'HOTEL', 'public', '24 hours daily', 'False', 'Ann Arbor', '48108', '3850 Research Park Dr', None, 'Non-Networked', 'J1772', None, None, '1', None, None, '2022-05-05'],
    ['216280', 'Mitsubishi Motor - Ann Arbor Lab', 'PARKING_LOT', 'public', '24 hours daily', 'False', 'Ann Arbor', '48108', '3735 Varsity Dr', None, 'Non-Networked', 'J1772', None, None, '2', None, None, '2022-05-05'],
    ['223001', 'A2DDA STATION 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223002', 'A2DDA STATION 3', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223003', 'A2DDA STATION 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223004', 'A2DDA STATION 4', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '324 Maynard St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223005', 'A2DDA ST 4123', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '320 Thompson St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223006', 'A2DDA STATION 4121', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '320 Thompson St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223007', 'A2DDA 500 E WASH 1', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '500 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223008', 'A2DDA 500 E WASH 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '500 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223009', 'A2DDA STATION 27', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '123E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223010', 'A2DDA STATION 28', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '115E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223011', 'A2DDA STATION 33', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '123E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223012', 'A2DDA STATION 22', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '115E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223013', 'A2DDA STATION 24', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '115E W William St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223014', 'A2DDA STATION 18', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223015', 'A2DDA STATION 19', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223016', 'A2DDA STATION 20', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223017', 'A2DDA STATION 13', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '120 W Ann St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223018', 'A2DDA STATION 17', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223019', 'A2DDA STATION 15', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '220 N Ashley St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223020', 'A2DDA STATION 12', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '120 W Ann St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223021', 'A2DDA STATION 26', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223022', 'A2DDA STATION 8', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223023', 'A2DDA STATION 21', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223024', 'A2DDA STATION 16', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223025', 'A2DDA STATION 25', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223026', 'A2DDA STATION 23', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223027', 'A2DDA STATION 6', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '650 S Forest Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223028', 'A2DDA STATION 31', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223029', 'A2DDA STATION 11', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223030', 'A2DDA STATION 9', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223031', 'A2DDA STATION 29', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223032', 'A2DDA STATION 32', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223033', 'A2DDA STATION 30', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223034', 'A2DDA STATION 7', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223035', 'A2DDA STATION 5', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223036', 'A2DDA STATION 10', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '319 S 5th Ave', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223038', 'A2DDA E WASH CT4K', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '123 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['223039', 'A2DDA E WASH CT4K 2', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '123 E Washington St', None, 'ChargePoint Network', 'J1772', None, None, '2', None, None, '2022-09-26'],
    ['228549', 'Shell', None, 'public', '24 hours daily', None, 'Ann Arbor', '48104', '2991 S State St', None, 'eVgo Network', 'CHADEMO, J1772COMBO', '1', None, None, None, None, '2022-09-26'],
    ['999999', 'U-M SI 506 WALL STREET #999999 (TEST RECORD)', None, 'public', '24 hours daily', None, 'Ann Arbor', '48105', '1041 Wall St', None, 'ChargePoint Network', 'CHADEMO, J1772COMBO', None, None, '10', None, None, '2022-09-26'],
    ]

# 1.1 CHALLENGE 01

headers = station_data[0]
stations = station_data[1:]

name_idx = headers.index('station_name')

meijer_count = 0
for station in stations:
    if 'meijer' in station[name_idx].lower():
    # if station[name_idx].lower().startswith('meijer'):
    # if station[name_idx].lower().find('meijer') > -1:
        meijer_count += 1

print(f"\n1.1. Meijer stations count = {meijer_count}")


# 1.0 IF-ELIF-ELSE

# Return list of unique "ev_connector_types" values (case sensitive)
ev_network_idx = headers.index('ev_network')

ev_network_vals = []
for station in stations:
    if station[ev_network_idx] not in ev_network_vals:
        ev_network_vals.append(station[ev_network_idx])

print(f"\n2.0 ev_network vals = {ev_network_vals}")

chargepoint_count = 0
elec_america_count = 0
ev_connect_count = 0
evgo_count = 0
greenlots_count = 0

for station in stations:
    if station[ev_network_idx].lower() == 'chargepoint network':
        chargepoint_count += 1
    elif station[ev_network_idx].lower() == 'electrify america':
        elec_america_count += 1
    elif station[ev_network_idx].lower() == 'ev connect':
        ev_connect_count += 1
    elif station[ev_network_idx].lower() == 'evgo network':
        evgo_count += 1
    elif station[ev_network_idx].lower() == 'greenlots':
        greenlots_count += 1
    else:
        continue # explicit but optional

# Pass multiple strings
print(f"\n2.0.1 Ann Arbor EV network charging station counts",
    f"\nChargePoint count = {chargepoint_count}",
    f"\nElectrify America count = {elec_america_count}",
    f"\nEV Connect count = {ev_connect_count}",
    f"\nEVgo count = {evgo_count}",
    f"\nGreenlots count = {greenlots_count}")


# Alternative (while loop)
# chargepoint_count = 0
# elec_america_count = 0
# ev_connect_count = 0
# evgo_count = 0
# greenlots_count = 0

# i = 0
# while i < len(stations):
#     if stations[i][ev_network_idx].lower() == 'chargepoint network':
#         chargepoint_count += 1
#     elif stations[i][ev_network_idx].lower() == 'electrify america':
#         elec_america_count += 1
#     elif stations[i][ev_network_idx].lower() == 'ev connect':
#         ev_connect_count += 1
#     elif stations[i][ev_network_idx].lower() == 'evgo network':
#         evgo_count += 1
#     elif stations[i][ev_network_idx].lower() == 'greenlots':
#         greenlots_count += 1
#     i += 1

# # Pass multiple strings
# print(f"\n2.0.2 Ann Arbor EV network charging station counts",
#     f"\nChargePoint count = {chargepoint_count}",
#     f"\nElectrify America count = {elec_america_count}",
#     f"\nEV Connect count = {ev_connect_count}",
#     f"\nEVgo count = {evgo_count}",
#     f"\nGreenlots count = {greenlots_count}")


# 2.1 CHALLENGE 02

last_confirmed_2020 = []
last_confirmed_2021 = []
last_confirmed_2022 = []
last_confirmed_other = []

for i in range(len(stations)):
    last_confirmed = stations[i][-1]
    if last_confirmed.startswith('2020'):
        last_confirmed_2020.append(stations[i][0])
    elif last_confirmed.startswith('2021'):
        last_confirmed_2021.append(stations[i][0])
    elif last_confirmed.startswith('2022'):
        last_confirmed_2022.append(stations[i][0])
    else:
        last_confirmed_other.append(stations[i][0])

# Alternative
# for i in range(len(stations)):
#     year = int(stations[i][-1].split('-')[0]) # int() cast is optional; string compare also works
#     if year == 2020:
#         last_confirmed_2020.append(stations[i][0])
#     elif year == 2021:
#         last_confirmed_2021.append(stations[i][0])
#     elif year == 2022:
#         last_confirmed_2022.append(stations[i][0])
#     else:
#         last_confirmed_other.append(stations[i][0])

print(f"\n2.1 Last confirmed 2020 (n={len(last_confirmed_2020)})")
pp.pprint(last_confirmed_2020)
print(f"\n2.1 Last confirmed 2021 (n={len(last_confirmed_2021)})")
pp.pprint(last_confirmed_2021)
print(f"\n2.1 Last confirmed 2022 (n={len(last_confirmed_2022)})")
pp.pprint(last_confirmed_2022)
print(f"\n2.1 Last confirmed other (n={len(last_confirmed_other)})")
pp.pprint(last_confirmed_other)


# 3.0 COMPOUND STATEMENTS

# 3.1 Dealing with None values

# Return list of unique "ev_level2_evse_num" values
# None values detected
level2_evse_idx = headers.index('ev_level2_evse_num') # lookup index value
ev_level2_evse_num_vals = []
for station in stations:
    if station[level2_evse_idx] not in ev_level2_evse_num_vals:
        ev_level2_evse_num_vals.append(station[level2_evse_idx])

print(f"\n3.0.1 ev_level2_evse_num unique values = {ev_level2_evse_num_vals}")

station_evse = []

# INCORRECT SYNTAX
# TODO Uncomment
# for station in stations:
#     if station[level2_evse_idx] is not None and int(station[level2_evse_idx]) >= 2 and <= 4: # SyntaxError: invalid syntax
#         station_evse.append(f"{station[1]}: Level2 EVSE = {station[level2_evse_idx]}")

# CORRECT SYNTAX
for station in stations:
    if station[level2_evse_idx] is not None and int(station[level2_evse_idx]) >= 2 and int(station[level2_evse_idx]) <= 4:
        station_evse.append(f"{station[1]}: Level2 EVSE = {station[level2_evse_idx]}")

print(f"\n3.0.2 Stations with 2-4 Level 2 EVSEs (n={len(station_evse)})")
pp.pprint(station_evse)

# PYTHONIC (INCLUDES TRUTH VALUE TEST)
station_evse.clear() # delete elements (avoid duplication)
for station in stations:
    if station[level2_evse_idx] and 2 <= int(station[level2_evse_idx]) <= 4:
        station_evse.append(f"{station[1]}: Level2 EVSE = {station[level2_evse_idx]}")

print(f"\n3.0.3 Stations with 2-4 Level 2 EVSE (Pythonic) (n={len(station_evse)})")
pp.pprint(station_evse)


# Handling ties when counting
most_evse = []
evse_count = 0
for station in stations:
    if station[level2_evse_idx] is None:
        continue # proceed to next station

    num = int(station[level2_evse_idx])
    if num > evse_count:
        evse_count = num # new
        most_evse.clear() # clear previous leader(s)
        most_evse.append(station) # new leader
    elif num == evse_count:
        most_evse.append(station) # tie
    else:
        continue # explicit but optional

print(f"\n3.0.4 Most Level 2 EVSE (count={evse_count})")
pp.pprint(most_evse)


# 3.2 LOGICAL AND OPERATOR

# U-M charging stations
um_count = 0
i = 0
while i < len(stations):
    if stations[i][name_idx].startswith('U-M'):
        um_count += 1
    i += 1

# Alternative (for loop)
# um_count = 0
# for station in stations:
#     if station[name_idx].startswith('U-M'):
#         um_count += 1

print(f"\n3.2.1 U-M charging stations = {um_count}")

# U-M charging stations filtered on a zip code
zip_idx = headers.index('zip')

um_count_48104 = 0
i = 0
while i < len(stations):
    if stations[i][name_idx].startswith('U-M') and int(stations[i][zip_idx]) == 48104:
        um_count_48104 += 1
    i += 1

# Alternative (for loop)
# um_count_48104 = 0
# for station in stations:
#     if station[name_idx].startswith('U-M') and int(station[zip_idx]) == 48104:
#         um_count_48104 += 1

print(f"\n3.2.2 U-M charging stations = {um_count_48104}")


# 3.3 CHALLENGE 03
street_idx = headers.index('street_address')

um_stations_greene_st = []
for station in stations:
    if station[name_idx].startswith('U-M') and 'greene st' in station[street_idx].lower():
        um_stations_greene_st.append(station)

print(f"\n3.3 U-M Greene St stations (n={len(um_stations_greene_st)}")
print(um_stations_greene_st)


# 3.4 LOGICAL OR OPERATOR

facility_type_idx = headers.index('facility_type')

a2dda_stations = []
for station in stations:
    name = station[name_idx]
    if name.startswith('A2DDA') or name.startswith('Ann Arbor Downtown Development Authority'):
        a2dda_stations.append(station[name_idx])

# Alternative
# i = 0
# while i < len(stations):
#     name = stations[i][name_idx]
#     if name.startswith('A2DDA') or name.startswith('Ann Arbor Downtown Development Authority'):
#         a2dda_stations.append(stations[i][name_idx])
#     i += 1

print(f"\n3.4. A2DDA stations (n={len(a2dda_stations)})")
print(a2dda_stations)


# 3.5 LOGICAL NOT OPERATOR

# Return list of unique "ev_network" values (case sensitive)
ev_network_vals = []
for station in stations:
    if station[ev_network_idx] not in ev_network_vals:
        ev_network_vals.append(station[ev_network_idx])

print(f"\n3.5.1 ev_network unique values (n={len(ev_network_vals)}) = {ev_network_vals}")

station_count = 0
for i in range(len(stations)):
    if stations[i][ev_network_idx] == 'ChargePoint Network':
        station_count += 1

print(f"\n3.5.2 ChargePoint network stations count = {station_count}")

# Count non ChargePoint network EV charging stations
station_count = 0
for i in range(len(stations)):
    if not stations[i][ev_network_idx] == 'ChargePoint Network':
        station_count += 1

print(f"\n3.5.3 Non ChargePoint network stations count = {station_count}")

# Alternative (!=)
station_count = 0
for i in range(len(stations)):
    if stations[i][ev_network_idx] != 'ChargePoint Network':
        station_count += 1

print(f"\n3.5.4 Non ChargePoint network stations count = {station_count}")


# 3.6 GROUPING RELATED EXPRESSIONS

# Return list of unique "facility_type" values (case sensitive)
facility_type_vals = []
for station in stations:
    if station[facility_type_idx] not in facility_type_vals:
        facility_type_vals.append(station[facility_type_idx])

print(f"\n3.6.1 facility_type unique values (n={len(facility_type_vals)}) = {facility_type_vals}")

# Dedicated parking garages and lots
parking_facilities = []
i = 0
while i < len(stations):
    facility_type = stations[i][facility_type_idx]
    if (facility_type is not None
        and (facility_type.lower() == 'parking_garage'
            or facility_type.lower() == 'parking_lot'
            or facility_type.lower() == 'pay_garage')):
        parking_facilities.append(f"{stations[i][1]} {stations[i][2]} {stations[i][3]}")
    i += 1

print(f"\n3.6.2 Parking facilities (n={len(parking_facilities)})")
pp.pprint(parking_facilities) # pretty list

# Alternative (membership in operator)
parking_facilities = []
facility_types = ('parking_garage', 'pay_garage', 'parking_lot')
for i in range(len(stations)):
    facility_type = stations[i][facility_type_idx]
    if facility_type is not None and facility_type.lower() in facility_types:
        parking_facilities.append(f"{stations[i][1]} {stations[i][2]} {stations[i][3]}")

print(f"\n3.6.3 Parking facilities (n={len(parking_facilities)})")
pp.pprint(parking_facilities)

# Parking facilities public only
access_code_idx = headers.index('access_code')

parking_facilities = []
for station in stations:
    facility_type = station[facility_type_idx]
    access_code = station[access_code_idx]
    if (facility_type is not None
        and (facility_type.lower() == 'parking_garage'
            or facility_type.lower() == 'parking_lot'
            or facility_type.lower() == 'pay_garage')
        and access_code.lower() == 'public'):
        parking_facilities.append(f"{station[1]} {station[2]} {station[3]}")

print(f"\n3.6.4 Public Parking facilities (n={len(parking_facilities)})")
pp.pprint(parking_facilities)

parking_facilities = []
for station in stations:
    facility_type = station[facility_type_idx]
    access_code = station[access_code_idx]
    if (facility_type is not None
        and (facility_type.lower() == 'parking_garage'
            or facility_type.lower() == 'parking_lot'
            or facility_type.lower() == 'pay_garage'
            and access_code.lower() == 'public')):
        parking_facilities.append(f"{station[1]} {station[2]} {station[3]}")

print(f"\n3.6.5 Public Parking facilities (n={len(parking_facilities)})")
pp.pprint(parking_facilities)


# 3.7 CHALLENGE 04

a2dda_stations = []
for station in stations:
    name = station[name_idx]
    street = station[street_idx]
    if ((name.startswith('A2DDA') or name.startswith('Ann Arbor Downtown Development Authority'))
        and ('forest' in street.lower() or 'maynard' in street.lower())):
        a2dda_stations.append(f"{name} {station[street_idx]}")

print(f"\n3.7 A2DDA stations on Maynard St or Forrest (n={len(a2dda_stations)})")
print(a2dda_stations)
