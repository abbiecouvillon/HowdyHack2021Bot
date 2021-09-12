'''Adding unique classes to a user's profile--Input: (int user_id, string user_name, string classname, string classnum, string classsec, list master_user_list--Returns updated master_user_list'''
def add_classes_to_profile(user_id, user_name, classname, classnum, classsec, master_user_list):
  what_adding_to_list = classname.upper() + " " + str(classnum) + " " + str(classsec) #makes the class into a string
  print(what_adding_to_list)
  
  id_list = []
  for i in master_user_list: #gets all the unique id's from the master list
    id_list.append(i[0])

  for i in master_user_list:
    
    temp_list = []
    if i[0] == user_id: #if user is the current name on the list
      if (what_adding_to_list not in i):
        i.append(what_adding_to_list)
      
      if (user_name != i[1]): #replacing username if they have changed it since last adding classes
        i.pop(1)
        i.insert(1, user_name)
      

    elif user_id not in id_list:
      temp_list.append(user_id)
      temp_list.append(user_name)
      temp_list.append(what_adding_to_list)
      master_user_list.append(temp_list)
      id_list.append(user_id) #adds the user_id of the user we just created a profile for to keep it from being created again
  return master_user_list

'''Removing unique classes from a user's profile--Input: (int user_id, String user_name, String classname, String/int classnum, String/int classsec, list master_user_list-- Returns updated master_user_list -- also updates the user's profile name if they have changed it since last call of the function'''
def remove_classes_from_profile(user_id, user_name, classname, classnum, classsec, master_user_list):
  what_removing_from_list = classname.upper() + " " + str(classnum) + " " + str(classsec)
  for i in master_user_list:
    if i[0] == user_id:
      if (what_removing_from_list in i):
        i.remove(what_removing_from_list)
    
    if (user_name != i[1]): #replacing username if they have changed it since last adding/removing classes
        i.pop(1)
        i.insert(1, user_name)
  return master_user_list

'''Checking if class name is legitimate, Input: Class Name (String)'''
def check_if_legit_name(name):
  name = name.upper()
  classNames = {
    1 : "AALO",
    2 : "ACCT",
    3 : "AERO",
    4 : "AERS",
    5 : "AFST",
    6 : "AGCJ",
    7 : "AGEC",
    8 : "AGLS",
    9 : "AGSC",
    10 : "AGSM",
    11 : "ALEC",
    12 : "ALED",
    13 : "ANSC",
    14 : "ANTH",
    15 : "ARAB",
    16 : "ARCH",
    17 : "AREN",
    18 : "ARTS",
    19 : "ASCC",
    20 : "ASIA",
    21 : "ASTR",
    22 : "ATMO",
    23 : "ATTR",
    24 : "BAEN",
    25 : "BEFB",
    26 : "BESC",
    27 : "BICH",
    28 : "BIMS",
    29 : "BIOL",
    30 : "BMEN",
    31 : "BOTN",
    32 : "BUSN",
    33 : "CARC",
    34 : "CEHD",
    35 : "CHEM",
    36 : "CHEN",
    37 : "CHIN",
    38 : "CLAS",
    39 : "CLEN",
    40 : "COMM",
    41 : "COSC",
    42 : "CSCE",
    43 : "CVEN",
    44 : "CYBR",
    45 : "DASC",
    46 : "DCED",
    47 : "DDHS",
    48 : "DIVE",
    49 : "ECEN",
    50 : "ECHE",
    51 : "ECMT",
    52 : "ECON",
    53 : "EDCI",
    54 : "EHRD",
    55 : "ENDG",
    56 : "ENDS",
    57 : "ENGL",
    58 : "ENGR",
    59 : "ENST",
    60 : "ENTC",
    61 : "ENTO",
    62 : "EPFB",
    63 : "EPSY",
    64 : "ESET",
    65 : "ESSM",
    66 : "EURO",
    67 : "EVEN",
    68 : "FILM",
    69 : "FINC",
    70 : "FIVS",
    71 : "FREN",
    72 : "FRSC",
    73 : "FSCI",
    74 : "FSTC",
    75 : "FYEX",
    76 : "GALV",
    77 : "GENE",
    78 : "GEOG",
    79 : "GEOL",
    80 : "GEOP",
    81 : "GEOS",
    82 : "GERM",
    83 : "HBRW",
    84 : "HEFB",
    85 : "HHUM",
    86 : "HISP",
    87 : "HIST",
    88 : "HLTH",
    89 : "HORT",
    90 : "HUMA",
    91 : "IBUS",
    92 : "IDIS",
    93 : "INST",
    94 : "INTS",
    95 : "ISEN",
    96 : "ISTM",
    97 : "ITAL",
    98 : "ITDE",
    99 : "JAPN",
    100 : "JOUR",
    101 : "KINE",
    102 : "KNFB",
    103 : "LAND",
    104 : "LBAR",
    105 : "LDEV",
    106 : "LING",
    107 : "LMAS",
    108 : "MARA",
    109 : "MARB",
    110 : "MARE",
    111 : "MARR",
    112 : "MARS",
    113 : "MART",
    114 : "MASC",
    115 : "MASE",
    116 : "MAST",
    117 : "MATH",
    118 : "MEEN",
    119 : "MEFB",
    120 : "MEPS",
    121 : "METR",
    122 : "MGMT",
    123 : "MICR",
    124 : "MKTG",
    125 : "MLSC",
    126 : "MMET",
    127 : "MODL",
    128 : "MSEN",
    129 : "MTDE",
    130 : "MUSC",
    131 : "MUST",
    132 : "MXET",
    133 : "NAUT",
    134 : "NRSC",
    135 : "NUEN",
    136 : "NURS",
    137 : "NUTR",
    138 : "NVSC",
    139 : "OCEN",
    140 : "OCNG",
    141 : "OCRE",
    142 : "PERF",
    143 : "PETE",
    144 : "PHIL",
    145 : "PHLT",
    146 : "PHYS",
    147 : "PLPA",
    148 : "POLS",
    149 : "PORT",
    150 : "POSC",
    151 : "PSYC",
    152 : "RDNG",
    153 : "RELS",
    154 : "RENR",
    155 : "RLEM",
    156 : "RPTS",
    157 : "RUSS",
    158 : "RWFM",
    159 : "SCEN",
    160 : "SCMT",
    161 : "SCSC",
    162 : "SEFB",
    163 : "SENG",
    164 : "SOCI",
    165 : "SOMS",
    166 : "SPAN",
    167 : "SPED",
    168 : "SPMT",
    169 : "STAT",
    170 : "TCMG",
    171 : "TEED",
    172 : "TEFB",
    173 : "UGST",
    174 : "URPN",
    175 : "VIBS",
    176 : "VIST",
    177 : "VLCS",
    178 : "VSCS",
    179 : "VTPB",
    180 : "VTPP",
    181 : "WFSC",
    182 : "WGST",
    183 : "ZOOL",
  }
  return (name in classNames.values())



'''Checking if the number associated with a class name is legitimate---Input: (String name, int number)---Output: Boolean'''
def check_if_legit_number (name, number):
  name = name.upper()
  class_names_and_numbers = [["AALO",285.00,289.00,485.00,489.00],
  ["ACCT",209.00,210.00,229.00,230.00,315.00,316.00,327.00,328.00,329.00,403.00,405.00,407.00,408.00,410.00,421.00,426.00,427.00,430.00,445.00,447.00,450.00,484.00,485.00,489.00,491.00],
  ["AERO",201.00,206.00,216.00,251.00,253.00,308.00,310.00,321.00,351.00,401.00,402.00,404.00,405.00,411.00,413.00,414.00,415.00,417.00,419.00,420.00,422.00,423.00,424.00,425.00,426.00,428.00,430.00,435.00,440.00,445.00,451.00,452.00,455.00,472.00,481.00,485.00,489.00,491.00],
  ["AERS",101.00,105.00,106.00,201.00,202.00,303.00,304.00,403.00,404.00,485.00],
  ["AFST",201.00,204.00,205.00,206.00,209.00,252.00,261.00,285.00,289.00,291.00,300.00,301.00,302.00,303.00,317.00,323.00,324.00,325.00,326.00,327.00,329.00,338.00,339.00,344.00,345.00,346.00,352.00,353.00,357.00,362.00,379.00,391.00,393.00,398.00,401.00,422.00,425.00,481.00,484.00,485.00,489.00,491.00],
  ["AGCJ",105.00,281.00,285.00,289.00,291.00,305.00,306.00,307.00,308.00,312.00,313.00,314.00,366.00,404.00,405.00,406.00,407.00,408.00,409.00,411.00,413.00,466.00,481.00,485.00,489.00,491.00,494.00],
  ["AGEC",101.00,105.00,117.00,203.00,216.00,217.00,223.00,285.00,289.00,291.00,314.00,315.00,316.00,317.00,323.00,324.00,330.00,341.00,409.00,413.00,414.00,415.00,416.00,420.00,422.00,423.00,424.00,425.00,429.00,430.00,431.00,432.00,434.00,440.00,447.00,448.00,452.00,453.00,460.00,481.00,484.00,485.00,489.00,491.00,495.00],
  ["AGLS",101.00,105.00,125.00,225.00,235.00,289.00,292.00,301.00,335.00,392.00,435.00,436.00,437.00,438.00,439.00,441.00,489.00,492.00],
  ["AGSC",285.00,289.00,291.00,302.00,305.00,373.00,380.00,383.00,402.00,405.00,425.00,436.00,481.00,484.00,485.00,489.00,491.00],
  ["AGSM",105.00,125.00,201.00,284.00,285.00,289.00,291.00,301.00,310.00,315.00,325.00,335.00,337.00,360.00,403.00,417.00,435.00,439.00,440.00,470.00,473.00,477.00,481.00,484.00,485.00,489.00,491.00],
  ["ALEC",201.00,285.00,289.00,291.00,350.00,380.00,399.00,412.00,425.00,450.00,460.00,485.00,489.00,491.00,494.00],
  ["ALED",125.00,202.00,225.00,285.00,289.00,291.00,301.00,313.00,322.00,323.00,324.00,339.00,340.00,341.00,344.00,380.00,400.00,401.00,422.00,424.00,426.00,440.00,441.00,481.00,485.00,489.00,491.00,494.00],
  ["ANSC",101.00,107.00,108.00,111.00,113.00,117.00,201.00,207.00,210.00,211.00,215.00,221.00,230.00,242.00,289.00,291.00,302.00,303.00,305.00,309.00,311.00,312.00,314.00,315.00,316.00,317.00,318.00,320.00,325.00,326.00,327.00,333.00,337.00,351.00,399.00,402.00,404.00,406.00,408.00,411.00,412.00,414.00,415.00,418.00,419.00,420.00,423.00,429.00,434.00,436.00,437.00,439.00,447.00,457.00,467.00,470.00,481.00,484.00,485.00,487.00,489.00,491.00,494.00,495.00,498.00],
  ["ANTH",201.00,202.00,204.00,205.00,210.00,222.00,225.00,226.00,229.00,285.00,289.00,291.00,300.00,301.00,302.00,304.00,305.00,308.00,312.00,313.00,316.00,317.00,318.00,323.00,324.00,330.00,335.00,340.00,350.00,351.00,353.00,354.00,360.00,370.00,401.00,402.00,403.00,404.00,405.00,409.00,410.00,412.00,415.00,417.00,418.00,419.00,421.00,423.00,424.00,434.00,435.00,436.00,437.00,440.00,444.00,445.00,446.00,447.00,448.00,458.00,461.00,484.00,485.00,489.00,491.00],
  ["ARAB",101.00,102.00,104.00,201.00,202.00,204.00,221.00,222.00,285.00,289.00,301.00,302.00,321.00,322.00,323.00,475.00,485.00,489.00,491.00],
  ["ARCH",205.00,206.00,212.00,213.00,216.00,221.00,246.00,249.00,250.00,260.00,281.00,291.00,305.00,317.00,327.00,328.00,330.00,331.00,335.00,345.00,346.00,347.00,350.00,353.00,360.00,381.00,405.00,494.00],
  ["AREN",175.00,200.00,300.00,320.00,330.00,370.00,399.00,401.00,402.00,440.00,485.00],
  ["ARTS",101.00,102.00,103.00,104.00,111.00,115.00,149.00,150.00,210.00,212.00,234.00,289.00,303.00,304.00,305.00,308.00,311.00,312.00,315.00,325.00,328.00,329.00,349.00,350.00,353.00,403.00,445.00,485.00,489.00],
  ["ASCC",1.00,2.00,3.00,4.00,5.00,101.00,102.00,289.00],
  ["ASIA",285.00,289.00,349.00,350.00,352.00,356.00,401.00,463.00,485.00,489.00,491.00],
  ["ASTR",101.00,111.00,314.00,320.00,401.00,403.00,420.00,485.00,489.00,491.00],
  ["ATMO",201.00,202.00,203.00,251.00,285.00,289.00,291.00,321.00,324.00,326.00,335.00,336.00,352.00,363.00,370.00,435.00,441.00,443.00,446.00,455.00,456.00,459.00,461.00,463.00,464.00,484.00,485.00,489.00,491.00],
  ["ATTR",201.00,202.00,301.00,302.00],
  ["BAEN",201.00,281.00,284.00,285.00,289.00,291.00,301.00,302.00,320.00,340.00,354.00,365.00,366.00,370.00,375.00,399.00,412.00,414.00,417.00,422.00,427.00,431.00,482.00,484.00,485.00,489.00,491.00],
  ["BEFB",425.00,426.00,470.00,472.00,474.00,476.00,482.00],
  ["BESC",201.00,204.00,285.00,291.00,311.00,314.00,320.00,357.00,367.00,401.00,402.00,403.00,411.00,431.00,481.00,484.00,485.00,489.00,491.00],
  ["BICH",101.00,285.00,303.00,410.00,411.00,440.00,441.00,450.00,456.00,460.00,461.00,464.00,485.00,489.00,491.00],
  ["BIMS",101.00,110.00,120.00,125.00,201.00,227.00,289.00,291.00,301.00,320.00,380.00,392.00,405.00,421.00,440.00,481.00,484.00,485.00,489.00,491.00],
  ["BIOL",100.00,101.00,111.00,112.00,113.00,206.00,213.00,413.00,440.00,444.00,445.00,450.00,451.00,454.00,455.00,456.00,461.00,462.00,466.00,467.00,480.00,481.00,484.00,485.00,487.00,489.00,491.00,492.00,495.00,496.00],
  ["BMEN",153.00,207.00,211.00,308.00,485.00,486.00,487.00,489.00,491.00],
  ["BOTN",289.00,291.00,485.00,491.00],
  ["BUSN",101.00,125.00,203.00,210.00,217.00,250.00,285.00,289.00,299.00,302.00,392.00,401.00,403.00,432.00,481.00,484.00,485.00,489.00,491.00],
  ["CARC",101.00,181.00,291.00,300.00,301.00,481.00,484.00,485.00,489.00,491.00],
  ["CEHD",100.00,101.00,289.00,291.00,300.00,491.00],
  ["CHEM",100.00,106.00,107.00,117.00,119.00,120.00,220.00,222.00,227.00,237.00,238.00,242.00,285.00,289.00,291.00,310.00,311.00,322.00,327.00,354.00,362.00,383.00,415.00,433.00,434.00,446.00,456.00,462.00,464.00,466.00,468.00,470.00,481.00,483.00,484.00,485.00,489.00,491.00],
  ["CHEN",204.00,206.00,216.00,285.00,289.00,301.00,304.00,308.00,320.00,322.00,323.00,324.00,354.00,364.00,399.00,409.00,410.00,422.00,425.00,426.00,430.00,431.00,482.00,485.00,489.00,491.00],
  ["CHIN",101.00,102.00,201.00,202.00,285.00,289.00,301.00,302.00,405.00,465.00,485.00,489.00,491.00],
  ["CLAS",101.00,102.00,121.00,122.00,211.00,220.00,221.00,222.00,236.00,250.00,251.00,261.00,262.00,285.00,289.00,291.00,311.00,312.00,313.00,320.00,321.00,322.00,330.00,352.00,353.00,354.00,371.00,372.00,410.00,415.00,417.00,418.00,426.00,427.00,428.00,429.00,444.00,485.00,489.00,491.00],
  ["CLEN",1.00,101.00,181.00,201.00,261.00,289.00,301.00,302.00,303.00,304.00],
  ["COMM",101.00,107.00,203.00,205.00,210.00,215.00,230.00,240.00,243.00,245.00,250.00,257.00,260.00,275.00,280.00,285.00,289.00,291.00,301.00,302.00,303.00,304.00,323.00,324.00,325.00,326.00,327.00,330.00,335.00,338.00,340.00,342.00,343.00,345.00,346.00,350.00,354.00,360.00,365.00,370.00,375.00,377.00,403.00,407.00,410.00,411.00,415.00,420.00,425.00,428.00,431.00,434.00,435.00,445.00,446.00,447.00,450.00,452.00,453.00,458.00,460.00,470.00,471.00,476.00,480.00,482.00,483.00,484.00,485.00,487.00,488.00,489.00,491.00,497.00],
  ["COSC",153.00,175.00,184.00,202.00,222.00,253.00,254.00,275.00,284.00,285.00,291.00,301.00,303.00,310.00,321.00,322.00,325.00,326.00,333.00,353.00,375.00,381.00,410.00,411.00,421.00,440.00,475.00,477.00,481.00,484.00,485.00,489.00,491.00,494.00],
  ["CSCE",110.00,111.00,120.00,206.00,221.00,222.00,285.00,289.00,291.00,305.00,360.00,399.00,402.00,403.00,410.00,411.00,412.00,413.00,416.00,420.00,421.00,426.00,429.00,430.00,431.00,433.00,434.00,435.00,436.00,438.00,440.00,441.00,442.00,443.00,487.00,489.00,491.00],
  ["CVEN",207.00,221.00,251.00,253.00,289.00,301.00,302.00,308.00,311.00,314.00,315.00,322.00,336.00,339.00,342.00,343.00,345.00,349.00,363.00,365.00,399.00,400.00,402.00,418.00,435.00,444.00,446.00,455.00,457.00,458.00,462.00,465.00,473.00,483.00,485.00,489.00,491.00],
  ["CYBR",201.00,285.00,289.00,291.00,403.00,477.00,484.00,485.00,489.00,491.00],
  ["DASC",418.00,485.00],
  ["DCED",168.00,202.00,203.00,222.00,260.00,271.00,301.00,303.00,304.00,306.00,308.00,361.00,372.00,400.00,401.00,402.00,405.00,462.00,473.00],
  ["DDHS",302.00,311.00,312.00,316.00,322.00,325.00,331.00,332.00,334.00,341.00,342.00,353.00,383.00,401.00,402.00,411.00,414.00,421.00,422.00,424.00,431.00,432.00,441.00,451.00,453.00,461.00,462.00,471.00,481.00,482.00],
  ["DIVE",250.00,251.00,260.00,330.00,331.00,357.00,410.00,489.00],
  ["ECEN",210.00,214.00,308.00,314.00,322.00,325.00,326.00,333.00,338.00,340.00,350.00,360.00,370.00,399.00,484.00,491.00],
  ["ECHE",291.00,491.00],
  ["ECMT",461.00,463.00,475.00],
  ["ECON",202.00,203.00,285.00,289.00,291.00,311.00,312.00,323.00,328.00,461.00,465.00,470.00,484.00,485.00,489.00,491.00],
  ["EDCI",285.00,289.00,291.00,353.00,354.00,371.00,485.00,489.00,491.00],
  ["EHRD",101.00,203.00,210.00,285.00,289.00,291.00,315.00,371.00,372.00,374.00,391.00,405.00,408.00,413.00,477.00,481.00,484.00,490.00,491.00],
  ["ENDG",485.00,489.00],
  ["ENDS",101.00,105.00,106.00,108.00,115.00,116.00,485.00,489.00,491.00],
  ["ENGL",103.00,104.00,107.00,202.00,203.00,204.00,205.00,206.00,207.00,209.00,210.00,211.00,212.00,219.00,220.00,221.00,222.00,227.00,228.00,231.00,232.00,235.00,241.00,251.00,253.00,262.00,285.00,289.00,291.00,292.00,303.00,304.00,305.00,306.00,308.00,309.00,311.00,313.00,314.00,315.00,316.00,317.00,318.00,320.00,321.00,322.00,323.00,324.00,329.00,330.00,331.00,333.00,334.00,335.00,336.00,337.00,338.00,339.00,340.00,342.00,343.00,345.00,347.00,348.00,350.00,351.00,352.00,353.00,354.00,355.00,356.00,357.00,358.00,359.00,360.00,361.00,362.00,365.00,372.00,373.00,374.00,375.00,376.00,377.00,378.00,379.00,385.00,386.00,390.00,391.00,392.00,393.00,394.00,395.00,396.00,401.00,403.00,412.00,414.00,415.00,431.00,433.00,435.00,460.00,461.00,462.00,474.00,481.00,482.00,484.00,485.00,489.00,491.00,497.00],
  ["ENGR",101.00,102.00,151.00,181.00,216.00,217.00,251.00,260.00,262.00,270.00,281.00,285.00,289.00,291.00,301.00,302.00,311.00,312.00,350.00,351.00,381.00,385.00,399.00,401.00,402.00,410.00,421.00,450.00,451.00,461.00,462.00,470.00,482.00,484.00,485.00,489.00,491.00,499.00],
  ["ENST",291.00,491.00],
  ["ENTC",289.00,399.00,481.00,484.00,485.00,489.00,491.00],
  ["ENTO",101.00,102.00,201.00,208.00,209.00,210.00,285.00,289.00,291.00,300.00,450.00,451.00,482.00,484.00,485.00,489.00,491.00],
  ["EPFB",210.00,301.00,401.00],
  ["EPSY",284.00,289.00,291.00,320.00,321.00,430.00,431.00,432.00,433.00,435.00,459.00,484.00,485.00,489.00,491.00],
  ["ESET",210.00,211.00,219.00,269.00,300.00,315.00,319.00,329.00,333.00,349.00,350.00,352.00,355.00,359.00,366.00,369.00,400.00,415.00,419.00,420.00,455.00,462.00,469.00],
  ["ESSM",102.00,201.00,203.00,281.00,291.00,300.00,301.00,302.00,303.00,304.00,305.00,306.00,307.00,308.00,309.00,310.00,311.00,313.00,314.00,315.00,316.00,317.00,318.00,319.00,320.00,324.00,351.00,405.00,651.00],
  ["EURO",285.00,289.00,291.00,405.00,441.00,442.00,443.00,444.00,446.00,447.00,484.00,485.00,489.00,491.00],
  ["EVEN",201.00,301.00,302.00,308.00,311.00,320.00,339.00,399.00,400.00,401.00,402.00,413.00,458.00,462.00,463.00,466.00],
  ["FILM",215.00,251.00,285.00,299.00,324.00,343.00,345.00,349.00,351.00,356.00,358.00,376.00,394.00,398.00,401.00,402.00,405.00,406.00,415.00,417.00,425.00,435.00,445.00,455.00,465.00,469.00,481.00,484.00,485.00,489.00,491.00],
  ["FINC",201.00,210.00,211.00,267.00,268.00,285.00,341.00,342.00,345.00,346.00,351.00,361.00,368.00,371.00,381.00,409.00,422.00,423.00,424.00,425.00,426.00,427.00,428.00,435.00,436.00,440.00,441.00,443.00,445.00,446.00,447.00,448.00,449.00,462.00,463.00,464.00,465.00,466.00,468.00,472.00,475.00,484.00,485.00,489.00],
  ["FIVS",101.00,102.00,123.00,205.00,285.00,289.00,291.00,308.00,316.00,401.00,482.00,484.00,485.00,489.00,491.00],
  ["FREN",101.00,102.00,201.00,202.00,221.00,222.00,285.00,289.00,300.00,301.00,306.00,311.00,321.00,322.00,336.00,375.00,418.00,422.00,425.00,481.00,485.00,489.00,491.00],
  ["FRSC",420.00,421.00],
  ["FSCI",281.00,285.00,289.00,334.00,485.00,489.00,491.00],
  ["FSTC",201.00,204.00,210.00,285.00,289.00,291.00,300.00,305.00,307.00,311.00,312.00,313.00,314.00,315.00,320.00,324.00,326.00,327.00,330.00,331.00,401.00,405.00,406.00,410.00,417.00,420.00,422.00,444.00,446.00,457.00,470.00,481.00,485.00,487.00,489.00,491.00],
  ["FYEX",101],
  ["GALV",101.00,201.00,300.00,301.00,401.00],
  ["GENE",101.00,285.00,301.00,302.00,320.00,404.00,405.00,406.00,411.00,412.00,419.00,420.00,440.00,464.00,485.00,489.00,491.00],
  ["GEOG",201.00,202.00,203.00,205.00,213.00,215.00,232.00,285.00,289.00,291.00,301.00,304.00,305.00,306.00,309.00,311.00,312.00,320.00,323.00,324.00,325.00,327.00,330.00,331.00,335.00,352.00,355.00,360.00,361.00,370.00,380.00,390.00,391.00,392.00,398.00,400.00,401.00,404.00,405.00,406.00,420.00,430.00,434.00,435.00,440.00,442.00,450.00,461.00,462.00,467.00,475.00,476.00,477.00,478.00,479.00,484.00,485.00,489.00,491.00],
  ["GEOL",101.00,104.00,106.00,150.00,152.00,180.00,203.00,207.00,208.00,210.00,250.00,285.00,289.00,291.00,300.00,302.00,306.00,309.00,312.00,320.00,330.00,350.00,352.00,360.00,404.00,410.00,412.00,416.00,420.00,440.00,450.00,451.00,478.00,481.00,484.00,485.00,489.00,491.00],
  ["GEOP",170.00,291.00,313.00,341.00,361.00,413.00,421.00,435.00,470.00,475.00,484.00,485.00,489.00,491.00],
  ["GEOS",101.00,105.00,110.00,205.00,210.00,289.00,291.00,301.00,370.00,380.00,401.00,405.00,410.00,430.00,431.00,442.00,443.00,444.00,470.00,471.00,481.00,483.00,484.00,485.00,489.00,491.00],
  ["GERM",101.00,102.00,104.00,201.00,202.00,204.00,221.00,222.00,285.00,289.00,310.00,311.00,315.00,316.00,321.00,322.00,331.00,332.00,333.00,334.00,336.00,362.00,410.00,411.00,435.00,437.00,440.00,441.00,485.00,489.00,491.00],
  ["HBRW",101.00,102.00,285.00,289.00],
  ["HEFB",222.00,324.00,325.00,450.00],
  ["HHUM",107.00,482.00],
  ["HISP",201.00,204.00,205.00,206.00,250.00,260.00,262.00,285.00,289.00,291.00,352.00,362.00,363.00,471.00,474.00,485.00,489.00,491.00],
  ["HIST",101.00,102.00,103.00,104.00,105.00,106.00,107.00,210.00,212.00,213.00,214.00,220.00,221.00,222.00,225.00,226.00,230.00,232.00,234.00,236.00,242.00,258.00,280.00,285.00,289.00,291.00,300.00,301.00,302.00,303.00,304.00,305.00,307.00,308.00,316.00,319.00,320.00,321.00,322.00,326.00,327.00,330.00,331.00,333.00,334.00,335.00,336.00,337.00,338.00,339.00,341.00,342.00,343.00,344.00,345.00,346.00,347.00,348.00,349.00,350.00,352.00,353.00,356.00,357.00,359.00,360.00,361.00,362.00,363.00,364.00,365.00,366.00,367.00,368.00,369.00,370.00,371.00,372.00,373.00,374.00,376.00,401.00,402.00,404.00,405.00,406.00,407.00,409.00,410.00,411.00,412.00,416.00,418.00,419.00,420.00,421.00,425.00,426.00,427.00,428.00,429.00,431.00,432.00,433.00,435.00,436.00,437.00,438.00,439.00,441.00,442.00,443.00,444.00,445.00,447.00,448.00,449.00,450.00,451.00,452.00,453.00,455.00,456.00,458.00,459.00,460.00,461.00,462.00,463.00,464.00,468.00,469.00,470.00,473.00,474.00,475.00,476.00,477.00,481.00,485.00,489.00,491.00,497.00],
  ["HLTH",210.00,214.00,216.00,221.00,222.00,231.00,236.00,240.00,285.00,291.00,331.00,332.00,333.00,334.00,335.00,342.00,353.00,354.00,403.00,405.00,407.00,410.00,415.00,421.00,425.00,429.00,440.00,445.00,481.00,482.00,484.00,485.00,489.00,491.00],
  ["HORT",201.00,202.00,203.00,281.00,291.00,301.00,302.00,306.00,308.00,315.00,319.00,325.00,326.00,328.00,332.00,335.00,360.00,400.00,404.00,416.00,418.00,419.00,420.00,421.00,423.00,424.00,425.00,426.00,428.00,429.00,431.00,432.00,435.00,440.00,442.00,446.00,450.00,451.00,452.00,453.00,454.00,460.00,481.00,484.00,485.00,489.00,491.00],
  ["HUMA",304.00,321.00,485.00,489.00],
  ["IBUS",285.00,289.00,301.00,401.00,402.00,409.00,430.00,440.00,445.00,446.00,450.00,452.00,453.00,455.00,456.00,457.00,459.00,484.00,485.00,489.00],
  ["IDIS",240.00,330.00,340.00,343.00,344.00,421.00,424.00,433.00,434.00,444.00,464.00,481.00,484.00,485.00,489.00],
  ["INST",210.00,222.00,291.00,301.00,362.00,363.00,491.00],
  ["INTS",201.00,205.00,211.00,215.00,251.00,261.00,285.00,289.00,300.00,301.00,311.00,321.00,401.00,403.00,405.00,407.00,409.00,410.00,481.00,489.00,491.00,497.00],
  ["ISEN",101.00,210.00,230.00,281.00,285.00,289.00,291.00,302.00,303.00,310.00,311.00,320.00,323.00,330.00,340.00,350.00,355.00,360.00,370.00,399.00,405.00,408.00,410.00,411.00,413.00,414.00,416.00,425.00,427.00,433.00,434.00,440.00,442.00,450.00,453.00,460.00,485.00,489.00,491.00],
  ["ISTM",209.00,210.00,250.00,281.00,310.00,313.00,315.00,320.00,325.00,360.00,380.00,381.00,410.00,415.00,420.00,425.00,440.00,450.00,455.00,481.00,482.00,484.00,485.00,489.00,601.00,610.00,612.00,615.00,620.00,622.00,624.00,630.00,631.00,635.00,637.00,643.00,645.00,650.00,652.00,655.00,660.00,670.00,680.00,681.00,682.00,684.00,685.00,689.00,705.00],
  ["ITAL",101.00,102.00,201.00,202.00,251.00,285.00,289.00,303.00,321.00,322.00,452.00,453.00,455.00,456.00,485.00,489.00,491.00],
  ["ITDE",201.00,285.00,289.00,291.00,301.00,399.00,401.00,402.00,485.00,489.00,491.00,499.00],
  ["JAPN",101.00,102.00,201.00,202.00,285.00,289.00,291.00,301.00,302.00,325.00,401.00,402.00,485.00,489.00,491.00],
  ["JOUR",102.00,200.00,203.00,215.00,230.00,250.00,285.00,289.00,291.00,301.00,307.00,317.00,341.00,359.00,365.00,450.00,451.00,455.00,458.00,468.00,484.00,485.00,489.00,490.00,491.00],
  ["KINE",120.00,223.00,240.00,260.00,271.00,282.00,285.00,289.00,291.00,302.00,306.00,307.00,308.00,311.00,312.00,314.00,317.00,318.00,319.00,320.00,321.00,324.00,325.00,334.00,335.00,340.00,351.00,355.00,361.00,372.00,386.00,403.00,404.00,406.00,407.00,425.00,426.00,427.00,429.00,431.00,433.00,435.00,439.00,462.00,473.00,482.00,483.00,484.00,485.00,489.00,491.00],
  ["KNFB",222.00,315.00,324.00,325.00,416.00,450.00],
  ["LAND",101.00,111.00,112.00,210.00,211.00,212.00,231.00,232.00,240.00,241.00,291.00,301.00,311.00,312.00,331.00,412.00,431.00,484.00,485.00,489.00,491.00,494.00],
  ["LBAR",181.00,200.00,203.00,204.00,285.00,289.00,291.00,300.00,330.00,331.00,332.00,392.00,400.00,484.00,485.00,489.00,491.00],
  ["LDEV",485.00,489.00],
  ["LING",209.00,291.00,307.00,310.00,403.00,481.00,485.00,489.00,491.00],
  ["LMAS",201.00,285.00,289.00,291.00,422.00,468.00,484.00,485.00,489.00,491.00],
  ["MARA",201.00,205.00,212.00,250.00,281.00,285.00,289.00,301.00,311.00,342.00,345.00,346.00,350.00,363.00,373.00,401.00,402.00,403.00,416.00,421.00,424.00,435.00,440.00,450.00,466.00,470.00,475.00,484.00,485.00,489.00,491.00,493.00],
  ["MARB",101.00,215.00,285.00,289.00,301.00,302.00,303.00,310.00,360.00,400.00,401.00,403.00,405.00,407.00,408.00,409.00,410.00,411.00,414.00,415.00,416.00,420.00,423.00,425.00,426.00,430.00,433.00,435.00,437.00,438.00,445.00,460.00,466.00,482.00,484.00,485.00,489.00,491.00],
  ["MARE",100.00,111.00,112.00,200.00,202.00,205.00,206.00,207.00,209.00,210.00,211.00,217.00,242.00,243.00,261.00,285.00,289.00,300.00,305.00,306.00,307.00,309.00,312.00,313.00,315.00,317.00,318.00,350.00,399.00,400.00,401.00,402.00,405.00,424.00,434.00,437.00,441.00,442.00,443.00,451.00,452.00,459.00,481.00,484.00,485.00,489.00,491.00],
  ["MARR",101.00,102.00,200.00,300.00,400.00,451.00,452.00,481.00],
  ["MARS",102.00,210.00,252.00,280.00,281.00,285.00,289.00,303.00,305.00,306.00,310.00,325.00,330.00,340.00,350.00,360.00,361.00,365.00,370.00,408.00,410.00,412.00,415.00,420.00,423.00,425.00,426.00,428.00,430.00,431.00,432.00,435.00,440.00,450.00,456.00,460.00,491.00],
  ["MART",103.00,115.00,200.00,201.00,204.00,205.00,208.00,210.00,212.00,213.00,215.00,265.00,285.00,289.00,300.00,303.00,321.00,350.00,400.00,401.00,403.00,404.00,410.00,484.00,485.00,489.00,491.00,498.00],
  ["MASC",320.00,351.00,420.00,450.00],
  ["MASE",400.00,401.00,407.00,410.00,485.00,489.00,491.00],
  ["MAST",101.00,220.00,226.00,230.00,240.00,252.00,265.00,270.00,289.00,321.00,333.00,336.00,340.00,345.00,350.00,354.00,365.00,369.00,371.00,411.00,425.00,441.00,470.00,480.00,481.00,484.00,485.00,489.00,491.00],
  ["MATH",102.00,140.00,168.00,171.00,172.00,200.00,221.00,251.00,253.00,281.00,285.00,289.00,291.00,300.00,302.00,304.00,323.00,325.00,365.00,366.00,367.00,375.00,376.00,396.00,401.00,403.00,467.00,469.00,470.00,471.00,472.00,478.00,482.00,485.00,489.00,490.00,491.00],
  ["MEEN",201.00,210.00,221.00,251.00,253.00,260.00,308.00,315.00,344.00,345.00,357.00,360.00,361.00,363.00,364.00,365.00,368.00,381.00,399.00,401.00,461.00,464.00,467.00,469.00,471.00,472.00,475.00,477.00,480.00,485.00,489.00,490.00,491.00],
  ["MEFB",351.00,450.00,470.00,490.00,497.00],
  ["MEPS",291.00,313.00,411.00,485.00,489.00,491.00],
  ["METR",302],
  ["MGMT",209.00,261.00,289.00,309.00,311.00,312.00,363.00,372.00,373.00,376.00,422.00,424.00,425.00,427.00,430.00,432.00,435.00,439.00,440.00,450.00,452.00,453.00,457.00,460.00,461.00,464.00,465.00,466.00,470.00,475.00,476.00,477.00,478.00,479.00,481.00,484.00,485.00,489.00],
  ["MICR",289.00,291.00,489.00,491.00],
  ["MKTG",298.00,299.00,321.00,322.00,323.00,325.00,326.00,335.00,336.00,345.00,347.00,401.00,402.00,409.00,425.00,426.00,427.00,430.00,431.00,432.00,435.00,436.00,437.00,438.00,440.00,441.00,442.00,443.00,444.00,445.00,447.00,448.00,484.00,485.00,489.00],
  ["MLSC",121.00,122.00,221.00,222.00,321.00,322.00,421.00,422.00,485.00,489.00,491.00],
  ["MMET",105.00,181.00,201.00,206.00,207.00,275.00,281.00,301.00,303.00,307.00,313.00,320.00,361.00,363.00,376.00,380.00,383.00,401.00,402.00,405.00,410.00,412.00,414.00,418.00,422.00,429.00,463.00],
  ["MODL",221.00,222.00,285.00,289.00,485.00,489.00],
  ["MSEN",201.00,206.00,210.00,413.00,415.00,418.00,420.00,426.00,430.00,440.00,444.00,446.00,458.00,470.00,472.00,484.00,485.00,489.00,491.00],
  ["MTDE",285.00,291.00,333.00,380.00,381.00,430.00,432.00,440.00,441.00,442.00,443.00,446.00,450.00,451.00,480.00,485.00,489.00,491.00],
  ["MUSC",200.00,280.00,282.00,283.00,290.00,400.00],
  ["MUST",221],
  ["MXET",300.00,375.00,400.00,462.00,635.00,681.00,684.00,685.00,689.00,691.00,692.00],
  ["NAUT",200.00,204.00,300.00,302.00,400.00],
  ["NRSC",101.00,102.00,201.00,235.00,277.00,289.00,311.00,320.00,332.00,340.00,350.00,360.00,401.00,407.00,434.00,440.00,444.00,450.00,485.00,489.00,491.00],
  ["NUEN",101.00,102.00,201.00,251.00,265.00,289.00,301.00,302.00,308.00,309.00,315.00,329.00,330.00,405.00,406.00,461.00,465.00,475.00,479.00,481.00,485.00,489.00,491.00],
  ["NURS",301.00,305.00,306.00,307.00,312.00,313.00,314.00,315.00,316.00,320.00,323.00,385.00,386.00,405.00,411.00,412.00,413.00,420.00,421.00,424.00,430.00,431.00,432.00,434.00,456.00,457.00,460.00,461.00,462.00,463.00,464.00,465.00,466.00,467.00,468.00,481.00,489.00,491.00],
  ["NUTR",202.00,203.00,204.00,210.00,211.00,222.00,285.00,289.00,291.00,300.00,301.00,303.00,304.00,320.00,365.00,404.00,407.00,410.00,412.00,430.00,440.00,450.00,469.00,471.00,475.00,481.00,485.00,489.00,491.00],
  ["NVSC",101.00,200.00,205.00,210.00,301.00,303.00,320.00,401.00,402.00,404.00,410.00,485.00],
  ["OCEN",201.00,213.00,214.00,221.00,308.00,311.00,336.00,341.00,344.00,345.00,351.00,352.00,361.00,362.00,363.00,399.00,400.00,401.00,402.00,403.00,405.00,406.00,407.00,408.00,410.00,411.00,415.00,421.00,451.00,459.00,460.00,461.00,463.00,465.00,467.00,474.00,481.00,485.00,489.00,491.00],
  ["OCNG",203.00,251.00,252.00,281.00,291.00,303.00,310.00,320.00,330.00,340.00,350.00,404.00,411.00,425.00,443.00,451.00,453.00,456.00,461.00,470.00,481.00,485.00,489.00,491.00],
  ["OCRE"],
  ["PERF",101.00,102.00,110.00,156.00,200.00,201.00,204.00,205.00,211.00,221.00,222.00,223.00,225.00,226.00,228.00,235.00,245.00,281.00,284.00,285.00,289.00,291.00,292.00,301.00,303.00,308.00,310.00,311.00,312.00,316.00,317.00,318.00,321.00,322.00,324.00,325.00,326.00,327.00,328.00,333.00,338.00,345.00,381.00,386.00,402.00,407.00,424.00,446.00,450.00,451.00,452.00,453.00,454.00,455.00,456.00,457.00,460.00,461.00,481.00,482.00,483.00,484.00,485.00,489.00,491.00,492.00],
  ["PETE",201.00,219.00,301.00,308.00,310.00,311.00,315.00,321.00,404.00,410.00,412.00,413.00,416.00,418.00,419.00,435.00,436.00,437.00,453.00,485.00,489.00,491.00],
  ["PHIL",107.00,111.00,205.00,208.00,240.00,251.00,252.00,255.00,282.00,283.00,285.00,289.00,291.00,305.00,307.00,314.00,315.00,320.00,330.00,331.00,332.00,334.00,336.00,341.00,342.00,351.00,352.00,353.00,361.00,371.00,375.00,376.00,381.00,409.00,410.00,411.00,412.00,413.00,414.00,415.00,416.00,417.00,418.00,419.00,424.00,425.00,464.00,465.00,470.00,480.00,482.00,484.00,485.00,489.00,491.00,497.00],
  ["PHLT",270.00,289.00,301.00,302.00,303.00,304.00,305.00,306.00,307.00,308.00,309.00,310.00,311.00,313.00,314.00,315.00,323.00,330.00,331.00,332.00,333.00,334.00,335.00,370.00,410.00,411.00,412.00,413.00,414.00,415.00,416.00,432.00,433.00,434.00,436.00,441.00,445.00,470.00,484.00,485.00,489.00,491.00],
  ["PHYS",101.00,102.00,109.00,119.00,123.00,125.00,148.00,150.00,201.00,202.00,205.00,206.00,207.00,216.00,217.00,221.00,251.00,253.00,308.00,309.00,331.00,332.00,401.00,408.00,412.00,414.00,416.00,418.00,425.00,426.00,485.00,489.00,491.00],
  ["PLPA",291.00,301.00,303.00,334.00,485.00,489.00,491.00],
  ["POLS",200.00,203.00,206.00,207.00,209.00,229.00,231.00,232.00,233.00,285.00,289.00,291.00,302.00,304.00,306.00,308.00,309.00,312.00,313.00,314.00,315.00,316.00,317.00,318.00,319.00,320.00,322.00,323.00,324.00,325.00,326.00,327.00,328.00,333.00,335.00,338.00,340.00,342.00,347.00,349.00,350.00,352.00,353.00,355.00,357.00,358.00,359.00,362.00,364.00,365.00,366.00,367.00,368.00,369.00,375.00,412.00,413.00,415.00,420.00,423.00,424.00,429.00,432.00,435.00,439.00,440.00,447.00,454.00,455.00,461.00,462.00,475.00,481.00,484.00,485.00,489.00,491.00,497.00],
  ["PORT",101.00,102.00,201.00,202.00],
  ["POSC",201.00,285.00,289.00,291.00,302.00,304.00,308.00,309.00,313.00,319.00,326.00,333.00,381.00,405.00,406.00,411.00,412.00,414.00,427.00,429.00,444.00,454.00,481.00,484.00,485.00,489.00,491.00],
  ["PSYC",101.00,102.00,105.00,107.00,206.00,208.00,209.00,210.00,225.00,235.00,245.00,251.00,285.00,289.00,291.00,300.00,301.00,302.00,303.00,304.00,305.00,306.00,307.00,311.00,315.00,316.00,319.00,320.00,323.00,330.00,332.00,340.00,345.00,346.00,350.00,352.00,353.00,354.00,360.00,365.00,371.00,389.00,407.00,411.00,414.00,425.00,432.00,440.00,450.00,470.00,471.00,475.00,483.00,484.00,485.00,489.00,491.00],
  ["RDNG",291.00,351.00,373.00,460.00,465.00,467.00,473.00,490.00,491.00],
  ["RELS",200.00,202.00,209.00,212.00,220.00,221.00,222.00,251.00,257.00,285.00,289.00,291.00,304.00,312.00,317.00,321.00,326.00,331.00,340.00,347.00,356.00,360.00,365.00,366.00,392.00,403.00,418.00,419.00,420.00,425.00,436.00,464.00,471.00,474.00,480.00,481.00,484.00,485.00,489.00,491.00],
  ["RENR",205.00,215.00,345.00,375.00,400.00,405.00,651.00],
  ["RLEM",321],
  ["RPTS",201.00,209.00,291.00,300.00,301.00,302.00,304.00,307.00,308.00,311.00,316.00,320.00,321.00,323.00,324.00,331.00,336.00,340.00,370.00,371.00,380.00,381.00,382.00,401.00,402.00,403.00,404.00,408.00,411.00,421.00,426.00,444.00,460.00,472.00,476.00,478.00,481.00,484.00,485.00,489.00,491.00],
  ["RUSS",101.00,102.00,201.00,202.00,211.00,221.00,222.00,285.00,289.00,301.00,302.00,322.00,410.00,441.00,442.00,443.00,444.00,446.00,447.00,485.00,489.00,491.00],
  ["RWFM",202.00,305.00,321.00,345.00,349.00,357.00,370.00,401.00,421.00,422.00,423.00,424.00,425.00,444.00,445.00,446.00,461.00],
  ["SCEN",100.00,101.00,102.00,201.00,289.00,292.00,301.00,302.00,392.00,489.00,492.00],
  ["SCMT",300.00,364.00,375.00,380.00,390.00,455.00,465.00,468.00,484.00,485.00,489.00],
  ["SCSC",105.00,201.00,205.00,289.00,291.00,301.00,302.00,304.00,305.00,307.00,309.00,310.00,311.00,312.00,315.00,330.00,401.00,482.00,484.00,485.00,489.00,491.00],
  ["SEFB",420.00,425.00,430.00,499.00],
  ["SENG",309.00,310.00,312.00,321.00,422.00,430.00,455.00,460.00,477.00,485.00,489.00],
  ["SOCI",203.00,205.00,206.00,207.00,208.00,210.00,211.00,212.00,213.00,217.00,220.00,229.00,230.00,240.00,285.00,289.00,291.00,304.00,308.00,310.00,311.00,312.00,313.00,314.00,315.00,316.00,317.00,319.00,320.00,322.00,323.00,326.00,328.00,329.00,330.00,332.00,335.00,337.00,338.00,376.00,377.00,402.00,403.00,404.00,408.00,410.00,411.00,412.00,413.00,415.00,419.00,420.00,421.00,422.00,423.00,424.00,425.00,426.00,430.00,432.00,479.00,484.00,485.00,489.00,491.00],
  ["SOMS",111.00,180.00,181.00,280.00,281.00,289.00,380.00,381.00,481.00,482.00,485.00,486.00,487.00,489.00],
  ["SPAN",101.00,102.00,112.00,201.00,208.00,221.00,222.00,285.00,289.00,301.00,302.00,304.00,306.00,307.00,311.00,312.00,318.00,320.00,331.00,332.00,341.00,342.00,350.00,352.00,403.00,407.00,409.00,410.00,411.00,412.00,413.00,414.00,417.00,421.00,423.00,445.00,450.00,452.00,460.00,461.00,462.00,483.00,484.00,485.00,489.00,491.00],
  ["SPED",291.00,302.00,310.00,311.00,312.00,314.00,414.00,442.00,471.00,491.00],
  ["SPMT",217.00,220.00,225.00,230.00,260.00,262.00,265.00,270.00,272.00,285.00,289.00,291.00,295.00,304.00,316.00,319.00,321.00,330.00,333.00,334.00,336.00,337.00,340.00,360.00,362.00,364.00,366.00,370.00,372.00,374.00,402.00,412.00,420.00,421.00,422.00,423.00,450.00,460.00,462.00,470.00,472.00,481.00,482.00,483.00,484.00,485.00,489.00,491.00],
  ["STAT",182.00,201.00,203.00,301.00,302.00,303.00,307.00,312.00,315.00,360.00,404.00,406.00,408.00,414.00,415.00,421.00,424.00,426.00,436.00,438.00,445.00,446.00,459.00,482.00,483.00,484.00,485.00,489.00,491.00],
  ["TCMG",272.00,274.00,285.00,289.00,291.00,303.00,308.00,316.00,402.00,412.00,476.00,484.00,490.00,491.00],
  ["TEED",302.00,425.00],
  ["TEFB",273.00,322.00,324.00,371.00,401.00,404.00,406.00,407.00,410.00,467.00,499.00],
  ["UGST",1.00,181.00,182.00,211.00,285.00,311.00,405.00,484.00,485.00,491.00,492.00,497.00],
  ["URPN",201.00,202.00,203.00,210.00,220.00,240.00,291.00,302.00,310.00,320.00,325.00,326.00,330.00,331.00,340.00,360.00,361.00,369.00,370.00,371.00,401.00,409.00,483.00,484.00,485.00,489.00,491.00,493.00,494.00],
  ["VIBS",101.00,102.00,111.00,201.00,204.00,210.00,211.00,222.00,243.00,277.00,285.00,289.00,305.00,310.00,311.00,343.00,401.00,404.00,407.00,408.00,411.00,413.00,420.00,422.00,424.00,426.00,443.00,445.00,447.00,450.00,456.00,485.00,489.00],
  ["VIST",105.00,106.00,131.00,170.00,201.00,205.00,283.00,284.00,289.00,305.00,310.00,339.00,354.00,357.00,370.00,372.00,374.00,375.00,405.00,494.00],
  ["VLCS",422.00,485.00],
  ["VSCS",485],
  ["VTPB",212.00,221.00,285.00,289.00,301.00,327.00,334.00,405.00,407.00,409.00,438.00,456.00,460.00,485.00,487.00,489.00],
  ["VTPP",123.00,223.00,224.00,234.00,235.00,281.00,285.00,289.00,291.00,323.00,401.00,434.00,435.00,438.00,444.00,452.00,481.00,485.00,489.00,491.00],
  ["WFSC",101.00,291.00,300.00,450.00,451.00,454.00,457.00,462.00,481.00,484.00,485.00,489.00,491.00],
  ["WGST",200.00,207.00,210.00,213.00,285.00,289.00,291.00,300.00,303.00,307.00,310.00,315.00,316.00,317.00,318.00,323.00,330.00,332.00,333.00,342.00,343.00,367.00,374.00,394.00,401.00,403.00,404.00,407.00,409.00,410.00,411.00,420.00,421.00,422.00,424.00,428.00,430.00,445.00,452.00,455.00,461.00,462.00,463.00,473.00,474.00,476.00,477.00,481.00,484.00,485.00,489.00,491.00],
  ["ZOOL",289.00,291.00,489.00,491.00]]
  
  for i in class_names_and_numbers:
    if i[0] == name:
      for j in i:
        if j == number:
          return True;
  return False


def check_if_legit_class(name, number):
  if (check_if_legit_name(name) and check_if_legit_number(name, number)):
    return True
  else:
    return False


    