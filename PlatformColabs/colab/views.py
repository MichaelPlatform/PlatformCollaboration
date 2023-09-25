from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import serializers
from rest_framework import status

@api_view(["GET", "POST"])
def groupsapi(request):
    previous_data = request.data
    reason = previous_data["reason"]

    if request.method == 'POST':
        if reason == "group-create":
            serializer = GroupSerializer(data=previous_data)
            if serializer.is_valid():
                data = serializer.validated_data
                group_name = data.get("name")
                account_key = data.get("admin")
                group_description = data.get("description")

                instance = Groups(name=group_name, admin=account_key, description=group_description)
                manager = GroupsManager(members=[], max_members=10, ban_list=[])
                instance.save()
                manager.save()
                return Response({"message":"Group created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Missing, "group", "account_key", and "description" value.'}, status=status.HTTP_404_NOT_FOUND)

        elif reason == "group-delete":
            group_key = previous_data.get("key") 

            if group_key:
                to_delete = Groups.objects.filter(key=group_key)

                if to_delete:
                    to_delete.delete()
                    return Response({'message': 'Items deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message': 'Missing, "key" value.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "group-join":
            group_key = previous_data.get("key")
            group_name = previous_data.get("group")
            account_key = previous_data.get("account_key")
            validate_key = GroupsManager.objects.filter(key=group_key)

            if validate_key:
                manager = GroupsManager.objects.get(key=group_key)  
                items = manager.members
                ban_list = manager.ban_list
                if len(items) < 10 and account_key not in ban_list:
                    items.append(account_key)
                    manager.save()
                    return Response({'message': f'New user joined {group_name}.'}, status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({'message': 'Unable to join group. Group is already full.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Unable to join group. As group is not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "group-sendmessage":
            serializer = MessagesSerializer(data=previous_data)
            if serializer.is_valid():
                data = serializer.validated_data
                username = data.get("username")
                account_key = data.get("account_key")
                message = data.get("message")
                group_key = data.get("key")
                filter = GroupsManager.objects.filter(key=group_key)  
                manager = GroupsManager.objects.get(key=group_key)  
                items = manager.members

                if filter:
                    if account_key in items:
                        messages = Messages(group_key=group_key, account_key=account_key, username=username, message=message, sender="groups")
                        return Response({"key": group_key, "username": username, "message": message}, status=200)
                        messages.save()
                    else:
                        return Response({'message': f'{account_key} not found in group.'}, status=status.HTTP_400_BAD_REQUEST) 
                else:
                    return Response({'message': 'Group not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "group-ban":
            user = data.get("user")
            reason = data.get("reason")
            account_key = data.get("account_key")
            group_key = data.get("key")
            filter = GroupsManager.objects.filter(key=group_key)  
            manager = GroupsManager.objects.get(key=group_key)  
            items = manager.members
            ban_list = manager.ban_list
            admin = manager.admin

            if filter and admin == account_key:
                if user in items:
                    items.remove(user)
                    ban_list.append(user)
                    Punishment(punishment_type="ban", account_key=user, reason=reason)
                    return Response({'message': f'Successfully banned user.'}, status=status.HTTP_204_NO_CONTENT)
                    Punishment.save()
                else:
                    return Response({'message': 'User not found in group.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Either you are not a administrator or group not found.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Command unknown.'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        if reason == "group-getdata":
            all_data = Groups.objects.all()
            serializer = GroupSerializer(all_data, many=True)  
            return Response({"data": serializer.data}, status=200)

        elif reason == "group-getmessages":
            all_data = Messages.objects.all()
            serializer = MessagesSerializer(all_data, many=True)  
            return Response({"data": serializer.data}, status=200)
        
        elif reason == "group-punishments":
            all_data = Punishment.objects.all()
            serializer = PunishmentSerializer(all_data, many=True)  
            return Response({"data": serializer.data}, status=200)

        else:
            return Response({'message': 'Command unknown.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def teamsapi(request):
    previous_data = request.data
    reason = previous_data["reason"]

    if request.method == 'POST':
        if reason == "team-create":
            serializer = TeamSerializer(data=previous_data)
            if serializer.is_valid():
                data = serializer.validated_data
                team_name = data.get("name")
                account_key = data.get("admin")
                team_description = data.get("description")

                instance = Teams(name=team_name, admin=account_key, description=team_description)
                manager = TeamsManager(members=[], max_members=10, ban_list=[], fundraiser=[])
                instance.save()
                manager.save()
                return Response({"message":"Team created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Missing "name," "admin," or "description" value.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "team-delete":
            team_key = previous_data.get("key") 

            if team_key:
                to_delete = Teams.objects.filter(key=team_key)

                if to_delete:
                    to_delete.delete()
                    return Response({'message': 'Items deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message': 'Missing "key" value.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "team-join":
            team_key = previous_data.get("key")
            team_name = previous_data.get("team")
            account_key = previous_data.get("account_key")
            validate_key = TeamsManager.objects.filter(key=team_key)

            if validate_key:
                manager = TeamsManager.objects.get(key=team_key)  
                members = manager.members
                ban_list = manager.ban_list
                if len(members) < 50 and account_key not in ban_list:
                    members.append(account_key)
                    manager.save()
                    return Response({'message': f'New user joined {team_name}.'}, status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({'message': 'Unable to join team. Team is already full.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Unable to join team. Team is not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "team-sendmessage":  
            serializer = MessagesSerializer(data=previous_data)
            if serializer.is_valid():
                data = serializer.validated_data
                username = data.get("username")
                account_key = data.get("account_key")
                message = data.get("message")
                team_key = data.get("key") 
                filter = TeamsManager.objects.filter(key=team_key)  
                manager = TeamsManager.objects.get(key=team_key)  
                items = manager.members

                if filter:
                    if account_key in items:
                        messages = Messages(team_key=team_key, account_key=account_key, username=username, message=message, sender="teams")  # Change 'Messages' to 'Teams'
                        return Response({"key": team_key, "username": username, "message": message}, status=200)
                        messages.save()
                    else:
                        return Response({'message': f'{account_key} not found in team.'}, status=status.HTTP_400_BAD_REQUEST) 
                else:
                    return Response({'message': 'Team not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "team-addfundraiser":
            fundraiser = data.get("fundraiser")
            team_key = data.get("key")
            filter = TeamsManager.objects.filter(key=team_key)  
            manager = TeamsManager.objects.get(key=team_key)  

            if filter:
                items = manager.fundraiser
                if fundraiser not in items:
                    items.append(fundraiser)
                    return Response({'message': f'Added new fundraiser to list.'}, status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({'message': f'Fundraiser already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': f'Team not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "team-deletefundraiser":
            fundraiser = data.get("fundraiser")
            team_key = data.get("key")
            filter = TeamsManager.objects.filter(key=team_key)  
            manager = TeamsManager.objects.get(key=team_key)  

            if filter:
                items = manager.fundraiser
                if fundraiser in items:
                    items.remove(fundraiser)
                    return Response({'message': f'Removed item from global fundraiser.'}, status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({'message': f'Fundraiser not found.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': f'Team not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "team-getfundraisers":
            team_key = data.get("key")
            filter = TeamsManager.objects.filter(key=team_key)  
            manager = TeamsManager.objects.get(key=team_key)  

            if filter:
                items = manager.fundraiser
                return Response({'data': items}, status=200)
            else:
                return Response({'message': f'Team not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "team-ban": 
            user = data.get("user")
            reason = data.get("reason")
            account_key = data.get("account_key")
            team_key = data.get("key")  
            filter = TeamsManager.objects.filter(key=team_key)  
            manager = TeamsManager.objects.get(key=team_key)  
            items = manager.members
            ban_list = manager.ban_list
            admin = manager.admin

            if filter and admin == account_key:
                if user in items:
                    items.remove(user)
                    ban_list.append(user)
                    Punishment(punishment_type="ban", account_key=user, reason=reason)
                    return Response({'message': f'Successfully banned user.'}, status=status.HTTP_204_NO_CONTENT)
                    Punishment.save()
                else:
                    return Response({'message': 'User not found in team.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Either you are not an administrator or team not found.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Command unknown.'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        if reason == "team-getdata":
            all_data = Teams.objects.all()
            serializer = TeamSerializer(all_data, many=True)  
            return Response({"data": serializer.data}, status=200)

        elif reason == "team-getmessages":
            all_data = Messages.objects.all()
            serializer = MessagesSerializer(all_data, many=True)  
            return Response({"data": serializer.data}, status=200)
        
        elif reason == "team-punishments":
            all_data = Punishment.objects.all()
            serializer = PunishmentSerializer(all_data, many=True)  
            return Response({"data": serializer.data}, status=200)
        else:
            return Response({'message': 'Command unknown.'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "POST"])
def companyapi(request):
    previous_data = request.data
    reason = previous_data["reason"]

    if request.method == 'POST':
        if reason == "business-create":
            serializer = BusinessSerializer(data=previous_data)
            if serializer.is_valid():
                data = serializer.validated_data
                business_name = data.get("name")
                account_key = data.get("admin")
                business_description = data.get("description")

                instance = Businesses(name=business_name, admin=account_key, description=business_description)
                manager = BusinessesManager(members=[], max_members=300, ban_list=[], current_project=[], meetings=[])
                instance.save()
                manager.save()
                return Response({"message": "Business created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Missing, "name", "admin", and "description" value.'}, status=status.HTTP_404_NOT_FOUND)

        elif reason == "business-delete":
            business_key = previous_data.get("key") 

            if business_key:
                to_delete = Businesses.objects.filter(key=business_key)

                if to_delete:
                    to_delete.delete()
                    return Response({'message': 'Businesses deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message': 'Missing, "key" value.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "business-join":
            business_key = previous_data.get("key")
            business_name = previous_data.get("business")
            account_key = previous_data.get("account_key")
            validate_key = BusinessesManager.objects.filter(key=business_key)

            if validate_key:
                manager = BusinessesManager.objects.get(key=business_key)  
                items = manager.members
                ban_list = manager.ban_list
                if len(items) < 300 and account_key not in ban_list:
                    items.append(account_key)
                    manager.save()
                    return Response({'message': f'New user joined {business_name}.'}, status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({'message': 'Unable to join business. Business is already full.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Unable to join business. Business is not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "business-sendmessage":
            serializer = MessagesSerializer(data=previous_data)
            if serializer.is_valid():
                data = serializer.validated_data
                username = data.get("username")
                account_key = data.get("account_key")
                message = data.get("message")
                business_key = data.get("key")
                filter = BusinessesManager.objects.filter(key=business_key)  
                manager = BusinessesManager.objects.get(key=business_key)  
                items = manager.members

                if filter:
                    if account_key in items:
                        messages = Messages(business_key=business_key, account_key=account_key, username=username, message=message, sender="businesses")
                        return Response({"key": business_key, "username": username, "message": message}, status=200)
                        messages.save()
                    else:
                        return Response({'message': f'{account_key} not found in business.'}, status=status.HTTP_400_BAD_REQUEST) 
                else:
                    return Response({'message': 'Business not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "business-newproject":
            business_key = data.get("key")
            project = data.get("new_project")
            filter = BusinessesManager.objects.filter(key=business_key)  
            manager = BusinessesManager.objects.get(key=business_key) 

            if filter:
                items = manager.current_projects
                if project not in items:
                    items.append(project)
                else:
                    return Response({'message': 'Project already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Business not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "business-deleteproject":
            business_key = data.get("key")
            project = data.get("project")
            filter = BusinessesManager.objects.filter(key=business_key)  
            manager = BusinessesManager.objects.get(key=business_key) 

            if filter:
                items = manager.current_projects
                if project in items:
                    items.delete(project)
                else:
                    return Response({'message': 'Project not found'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Business not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "business-newmeeting":
            business_key = data.get("key")
            meeting = data.get("new_meeting")
            filter = BusinessesManager.objects.filter(key=business_key)  
            manager = BusinessesManager.objects.get(key=business_key) 

            if filter:
                items = manager.meetings
                if meeting not in items:
                    items.append(meeting)
                else:
                    return Response({'message': 'Meeting already exists.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Business not found.'}, status=status.HTTP_400_BAD_REQUEST)

        elif reason == "business-ban":
            user = data.get("user")
            reason = data.get("reason")
            account_key = data.get("account_key")
            business_key = data.get("key")
            filter = BusinessesManager.objects.filter(key=business_key)  
            manager = BusinessesManager.objects.get(key=business_key)  
            items = manager.members
            ban_list = manager.ban_list
            admin = manager.admin

            if filter and admin == account_key:
                if user in items:
                    items.remove(user)
                    ban_list.append(user)
                    Punishment(punishment_type="ban", account_key=user, reason=reason)
                    return Response({'message': f'Successfully banned user.'}, status=status.HTTP_204_NO_CONTENT)
                    Punishment.save()
                else:
                    return Response({'message': 'User not found in business.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Either you are not an administrator or business not found.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Command unknown.'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        if reason == "business-getdata":
            all_data = Businesses.objects.all()
            serializer = BusinessSerializer(all_data, many=True)  
            return Response({"data": serializer.data}, status=200)

        elif reason == "business-getmessages":
            all_data = Messages.objects.all()
            serializer = MessagesSerializer(all_data, many=True)  
            return Response({"data": serializer.data}, status=200)
        
        elif reason == "business-punishments":
            all_data = Punishment.objects.all()
            serializer = PunishmentSerializer(all_data, many=True)  
            return Response({"data": serializer.data}, status=200)

        else:
            return Response({'message': 'Command unknown.'}, status=status.HTTP_400_BAD_REQUEST)
