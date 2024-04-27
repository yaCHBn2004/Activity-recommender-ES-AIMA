from aima.logic import *

def inference_engine(kb, user_profile):
    current_user = user_profile["Name"]
    print(current_user, type(current_user))
    agenda = []
    agenda.append(expr(f"User({user_profile['Name']})"))
    agenda.append(expr(f"SocialInteraction({user_profile['social_interaction'] }, {user_profile['Name']})"))
    agenda.append(expr(f"ActivityType( {user_profile['ActivityType']} , {user_profile['Name']})"))
    agenda.append(expr(f"Age({user_profile['Age']}, {user_profile['Name']})"))
    agenda.append(expr(f"GoalTime({user_profile['goalTime']}, {user_profile['Name']})"))
    agenda.append(expr(f"MoneySpendingByMounth({str(user_profile['moneySpendingByMounth'])}, {user_profile['Name']})"))
    agenda.append(expr(f"MaterialNeeded({user_profile['materialNeeded']}, {user_profile['Name']})"))
    agenda.append(expr(f"Dev({user_profile['dev']}, {user_profile['Name']})")),
    agenda.append(expr(f"Place({user_profile['place']}, {user_profile['Name']})"))



    
    # kb.tell(expr(f"MealTypePref({user_profile['Name']}, {user_profile['MealTypePref']})"))
    # kb.tell(expr(f"User({user_profile['Name']})"))
    # kb.tell(expr(f"DietaryPreference({user_profile['Name']}, {user_profile['DietaryPreference']})"))
    # kb.tell(expr(f"Goal({user_profile['Name']}, {user_profile['Goal']})"))
    # kb.tell(expr(f"ActivityLevel({user_profile['Name']}, {user_profile['ActivityLevel']})"))

        
    memory = {}
    seen = set() 
    while agenda:
        p = agenda.pop(0)
        if p in seen:
            continue 
        seen.add(p)
        
        if fol_fc_ask(kb, p):
            print(f'{p} is true.')
            memory[p] = True
        else:
            print(f'{p} is false.')
            memory[p] = False

        if memory.get(expr(f"ActivityType(Mental, {current_user})"), False) and memory.get(expr(f"Dev(Brain, {current_user})"), False):
            agenda.append(expr(f'Type(Art, {current_user})'))

        if memory.get(expr(f"ActivityType(Mental, {current_user})"), False) and memory.get(expr(f"Dev(Soul, {current_user})"), False):
            agenda.append(expr(f'Type(Logical, {current_user})'))

        if memory.get(expr(f"ActivityType(Physical, {current_user})"), False) and memory.get(expr(f"Dev(Brain, {current_user})"), False):
            agenda.append(expr(f'Type(Strength, {current_user})'))

        if memory.get(expr(f"ActivityType(Physical, {current_user})"), False) and memory.get(expr(f"Dev(Soul, {current_user})"), False):
            agenda.append(expr(f'Type(Flexibility, {current_user})'))
        


        if memory.get(expr(f"SocialInteraction(Group, {current_user})"), False) :
            agenda.append(expr(f'SocialInteraction(NoMatter, {current_user})'))
        
        if memory.get(expr(f"SocialInteraction(Alone, {current_user})"), False) :
            agenda.append(expr(f'SocialInteraction(NoMatter, {current_user})'))
        



        if memory.get(expr(f"ActivityType(Mental, {current_user})"), False) and memory.get(expr(f"MoneySpendingByMounth(Free, {current_user})"), False) and memory.get(expr(f"GoalTime(Long, {current_user})"), False) :
            agenda.append(expr(f'Activity(Language_Learning, {current_user})'))

        if memory.get(expr(f"Type(Logical, {current_user})"), False) and memory.get(expr(f"Place(Interior ,  {current_user})"), False) and memory.get(expr(f"SocialInteraction(Alone, {current_user})"), False) and memory.get(expr(f"GoalTime(Long, {current_user})"), False):
            agenda.append(expr(f'Activity(Chess, {current_user})'))
        
        if memory.get(expr(f"MoneySpendingByMounth(Expensive, {current_user})"), False) and memory.get(expr(f"Age(Young,  {current_user})"), False) and memory.get(expr(f"GoalTime(Long, {current_user})"), False) and memory.get(expr(f"Safety(NoMatter ,  {current_user})"), False) and memory.get(expr(f"SocialInteraction(Group, {current_user})"), False):
            agenda.append(expr(f'Activity(Football, {current_user})'))
            
        if memory.get(expr(f"GoalTime(Long, {current_user})"), False) and memory.get(expr(f"MaterialNeeded(Moderate, {current_user})"), False):
            agenda.append(expr(f'Activity(Yoga, {current_user})'))
        
        if memory.get(expr(f"MoneySpendingByMounth(Free, {current_user})"), False) and memory.get(expr(f"Place(Interior,  {current_user})"), False) and memory.get(expr(f"Type(Logical, {current_user})"), False) or memory.get(expr(f"GoalTime(Short,  {current_user})"), False) and memory.get(expr(f"Type(Logical, {current_user})"), False):
            agenda.append(expr(f'Activity(Sudoku, {current_user})'))
        
        if memory.get(expr(f"Type(Art, {current_user})"), False) and memory.get(expr(f"GoalTime(Long, {current_user})"), False):
            agenda.append(expr(f'Activity(Music, {current_user})'))
        
        if memory.get(expr(f"Type(Art,  {current_user})"), False) and memory.get(expr(f"ActivityType(Physical, {current_user})"), False):
            agenda.append(expr(f'Activity(Dance, {current_user})'))
        
        if memory.get(expr(f"Place(Whatever,  {current_user})"), False) and memory.get(expr(f"Type(Art, {current_user})"), False):
            agenda.append(expr(f'Activity(Painting, {current_user})'))

        if memory.get(expr(f"Type(Strength,  {current_user})"), False) and memory.get(expr(f"Place(Exterior, {current_user})"), False):
            agenda.append(expr(f'Activity(Rock_Climbing, {current_user})'))
            
        if memory.get(expr(f"Place(Interior,  {current_user})"), False) and memory.get(expr(f"Type(Logical, {current_user})"), False):
            agenda.append(expr(f'Activity(Crossword_Puzzles, {current_user})'))
   
        if memory.get(expr(f"Place(Exterior,  {current_user})"), False) and memory.get(expr(f"MaterialNeeded(Expensive, {current_user})"), False)  and memory.get(expr(f"ActivityType(Physical, {current_user})"), False)  and memory.get(expr(f"SocialInteraction(Group, {current_user})"), False):
            agenda.append(expr(f'Activity(Hiking, {current_user})'))
   
        if memory.get(expr(f"Place(Exterior, {current_user})"), False)  and memory.get(expr(f"MaterialNeeded(VeryExpensive, {current_user})"), False)  and memory.get(expr(f"SocialInteraction(NoMatter, {current_user})"), False):
            agenda.append(expr(f'Activity(Photography, {current_user})'))
   
        if memory.get(expr(f"Type(Strength, {current_user})"), False)  :
            agenda.append(expr(f'Activity(Martial_Arts, {current_user})'))
    
        if memory.get(expr(f"Type(Strength, {current_user})"), False) and memory.get(expr(f"MoneySpendingByMounth(Moderate, {current_user})"), False)  :
            agenda.append(expr(f'Activity(Swimming, {current_user})'))
        
        if memory.get(expr(f"ActivityType(Mental, {current_user})"), False)  and memory.get(expr(f"MoneySpendingByMounth(VeryExpensive, {current_user})"), False)  and memory.get(expr(f"Place(Internal, {current_user})"), False):
            agenda.append(expr(f'Activity(Cooking, x) {current_user})'))
   
        if memory.get(expr(f"Type(Flexibility, {current_user})"), False) and memory.get(expr(f"MaterialNeeded(Expensive, {current_user})"), False)  :
            agenda.append(expr(f'Activity(Cycling, {current_user})'))
        
    return memory
