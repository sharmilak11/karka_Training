my_resume={"name":"sharmila",
           "email_id":"sharmi29103@gmail.com",
           "phone no":7092123534,
           "softskills":["communication","adatability","willingness to learn","decision making"],
           "hard_skills":["basic_computer_skill","network_marketing"],
           "educational_qualification":[{"Qualification":"sslc","Institute":"D.V.D hre,sec,school","place":"nagercoil","percentage":"85%"},                                         {"Qualification":"Hsc","Institute":"D.V.D hre,sec,school","place":"nagercoil","percentage":"70%"},
                                        {"Qualification":"Degree","Institute":"Government arts and science","place":"konam","percentage":"75%"}],
           "project":["Rfid scan entry","frame work of python","authentication"],
           "Experience":[{"company_name":"tata","role":"Help desk analyst","duration":1,},
                         {"company_name":"amazon","role":"Develop","duration":2},
                         {"company_name":"tata","role":"Help desk analyst","duration":1}],
           "hobbies":["lesening music","cooking","going to temple"],
           "Personal_Details":{"Fathers Name":"Kumaraswamy pillai",
                                "Fathers occupation":"coolie",
                               "Language Known":["tamil","english"],
                               "D.O.B":"29/1/2003",
                               "Gender":"Female",
                               "Martial status":"Married",
                               "Address":{"Door no":"1/25E",
                                           "Place":"Nettankodu",       
                                            "villagam":"pallathu villagam house",
                                            "post":"karankadu",
                                           "District":"Kanyakumari",
                                           "pincode":629809}}}

# for item in my_resume["educational_qualification"]:
# #  print(item)
#  a=(item["Qualification"])
#  b=(item["Institute"])
#  c=(item["place"])
#  d=(item["percentage"])
#  print(f'qualification:{a}')
#  print(f"institute:{b}"),
#  print(f"place:{c}")
#  print(f'percentage:{d}')
# print(my_resume)

# for i in my_resume['Personal_Details']:
    # print(i)
    # print(f'{i}:{my_resume["Personal_Details"][i]}')
    # print(my_resume["Personal_Details"][i])

for item in my_resume["Personal_Details"]["Address"]:
    # print(item) 
    print(f"{item}:{my_resume['Personal_Details']['Address'][item]}")