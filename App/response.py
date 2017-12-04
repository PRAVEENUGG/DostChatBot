##dict of response for each type of intent and entity pair
def searchBy_BEF_BCType(BEF_Name, BCType):
    return "Praveen1"

def searchBy_BEF_BCType(BEF_Name):
    bef_n = Organisation.nodes.get(ORG_NAME=BEF_Name)
    print("Inside search fro BEF")
    
    query_res = None
    for bcs in bef_n.bef.all():
        if query_res:
            query_res = query_res + bcs.BC_NAME + " "
        else:
            query_res = bcs_BC_NAME + " "
    
    return query_res
        
def searchBy_BC_Children(BC_Name):
    print("Inside search by BEF")
    bd = BusinessCapability.nodes.get(BC_NAME=BC_Name)
    print(bd)
    
    query_res = None
    for bc_bd in bd.bc_child.all():
        if query_res:
            query_res = query_res + bc_bd.BC_NAME + " "
        else:
            query_res = bc_bd.BC_Name + " "
    
    return query_res

response = {
    "greet":["text", "Hi, How can I help you?"],
    "goodbye":["text", "bye, It was nice talking to you"],
    "affirm":["text", "cool"],
    "BC_Info":["text", "Business Capabilities shows a blueprint of Novartis's value Chain. http://go/BCMap/Info for more details"],
    "intro":["text","I am Dost, your friendly TAD Bot. I currently have learnt about Business Capabilities & I can help you here. I plan to learn about other TAD areas soon!"],
    "BC_search":["method", {"BEF|BCType": searchBy_BEF_BCType, 
                            "BEF" : searchBy_BEF_BCType
                           }
                ]
}


