from neomodel import db, StructuredNode, StringProperty, RelationshipFrom, UniqueIdProperty, RelationshipTo, Relationship

class Organisation(StructuredNode):
    name = StringProperty()
    ORG_NAME = StringProperty(unique_index=True, required=True)
    LEAD_ARCH = StringProperty()
    ORG_TYPE = StringProperty()
    bef = RelationshipFrom('BusinessCapability', 'BEF') 

class BusinessCapability(StructuredNode):
    BC_ID = UniqueIdProperty()
    BC_NAME = StringProperty()
    BC_DESC = StringProperty()
    BC_TYPE = StringProperty()
    BC_LEVEL = StringProperty()
    bef = RelationshipTo(Organisation, 'BEF')
    bc_child = RelationshipTo('BusinessCapability', 'Child')
    app = RelationshipFrom('Applications', 'APP_BC')
    
class Applications(StructuredNode):
    APP_NAME = StringProperty()
    APP_ID = StringProperty()
    IS_ACTIVE = StringProperty()
    URL_TXT = StringProperty()
    GROUP_BUS_FUNC = StringProperty()
    APP_TYPE = StringProperty()
    APP_LIFE_STATUS = StringProperty()
    GXP_REL = StringProperty()
    MANAGER_UNIQUE_NAME = StringProperty()
    bc = RelationshipTo(BusinessCapability, 'APP_BC')    
 

class results():
    def get_results(intent,entities):
        print("inside get_results")
        call_method_type = None
        call_method_values= []
        print("intent is %s entities is %s" %(intent, entities))
        try:
            if entities:
                if response[intent][0] == 'method':
                    print("inside getting entities and values")
                    #build the call_method_type from entities dict
                    for k,v in entities.items():
                        if call_method_type:
                            call_method_type = call_method_type + "|" + k
                        else:
                            call_method_type = k
                        call_method_values.append(v)
                    print("got call_method %s and call_method_values %s" %(call_method_type, call_method_values))
                    call_method = response[intent][1][call_method_type]
                    # at this point use **kwargs
                    result = call_method(call_method_values[0])
            else:   
                print("inside checking for greet %s" % response[intent][1])
                result = response[intent][1]
             #result = "intent is %s entities is %s" %(intent, entities)
        except Exception as e:
            print(e)            
            result = e
        return result
    
    def __init__(self):
        print("Inside init method")
        self.intent = None
        self.entities = None
        db.set_connection('bolt://neo4j:abcd123@localhost:7687')       



def searchBy_BEF_BCType(BEF_Name, BCType):
    return "Praveen1"

def searchBy_BEF_BCType(BEF_Name):
    bef_n = Organisation.nodes.get(ORG_NAME=BEF_Name)
    print("Inside search fro BEF")
    
    query_res = None
    for bcs in bef_n.bef.all():
        if query_res:
            query_res = query_res + bcs.BC_NAME + "\n"
        else:
            query_res = bcs.BC_NAME + "\n"
    
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

##dict of response for each type of intent and entity pair
response = {
    "greet":["text", "Hi, How can I help you?"],
    "goodbye":["text", "bye, It was nice talking to you"],
    "affirm":["text", "cool"],
    "BC_info":["text", "Business Capabilities (also called BCMap, BC etc) shows a blueprint of Novartis's value Chain. Check <a href=\"http://go/BCMap/Info\">link</a> for more details"],
    "info":["text","I am Dost, your friendly Bot from TAD. My creators have taught me a few things about Business Capabilities. I can help you here. I intend to learn about other TAD areas soon!"],
    "BC_search":["method", {"BEF|BCType": searchBy_BEF_BCType, 
                            "BEF" : searchBy_BEF_BCType
                           }
                ]
}