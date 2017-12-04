# -*- coding: utf-8 -*-

from neomodel import db, StructuredNode, StringProperty, RelationshipFrom, UniqueIdProperty, RelationshipTo, Relationship
db.set_connection('bolt://neo4j:abcd123@localhost:7687')

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
 
    
dit = Organisation.nodes.get(name='TA&D')
for bcs in dit.bef.all():
    print(bcs.BC_NAME)

bd = BusinessCapability.nodes.get(BC_NAME='Clinical Lab Services')
print(bd)

for bc_bd in bd.bc_child.all():
    print(bc_bd.BC_ID) # all child belonging to BD


for app_bd in bd.app.all():
    print(app_bd) # all apps belonging to BD
    
appl = Applications.nodes.get(APP_ID = 39609)
print('Here %s' % appl)



