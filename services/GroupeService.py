import json
from database.config import db
from models.Groupe import Groupe

class GroupeService:

    @staticmethod
    def create_groupe(data):
        groupe = Groupe(**data)
        db.session.add(groupe)
        db.session.commit()
        return groupe
    
    @staticmethod
    def get_all_groupes():
        return Groupe.query.all()
    
    @staticmethod
    def get_groupe_by_id(idGroupe):
        return Groupe.query.get(idGroupe)
    
    @staticmethod
    def delete_groupe(idGroupe):
        groupe = Groupe.query.get(idGroupe)

        db.session.delete(groupe)
        db.session.commit()

        return groupe

    @staticmethod
    def update_groupe(id, name):
        groupe = Groupe.query.get(id)
        groupe.name = name
        db.session.commit()
        return groupe
    
    @staticmethod
    def get_children(id_group):
        group = Groupe.query.get(id_group)
        result = group.to_dict() 

        subgroups = Groupe.query.filter_by(id_group_parent=id_group).all()
        result_temp = []
        for subgroup in subgroups:
            # temp = subgroup.to_dict()
            # temp['children'] = []
            # temp['children'] = GroupeService.get_children(subgroup.id)
            result_temp.append( GroupeService.get_children(subgroup.id))
        
        if len(result_temp) != 0:
            result['children'] = result_temp
        return result
    
    def get_parents(id_group):
        group = Groupe.query.get(id_group)
        result_temp = None
        if group.id_group_parent:
            result_temp = GroupeService.get_parents(group.id_group_parent)
        result = group.to_dict()
        if result_temp:
            result['parent'] = result_temp

        return result
    
    @staticmethod
    def get_tree(id):
        group = Groupe.query.get(id)
        
        result = [group.id]
        children = GroupeService.get_children(id)
        current = [children]
        while len(current) !=0:
            if 'children' in current[0]:
                for child in current[0]['children']:
                    result.append(child['id'])
                    current.append(child)
            current.pop(0)


        parent = GroupeService.get_parents(id)
        while 'parent' in parent:
            parent = parent['parent']
            result.append(parent['id'])
        return result

        
            
        # parent = GroupeService.get_parents(id)
        

