from aima.logic import *

# Define a knowledge base
activity_kb = FolKB()

# Set of facts


activity_kb.tell(expr('Age(Teen, x)==>Age(Over10, x)'))
activity_kb.tell(expr('Age(Young, x)==>Age(Over10, x)'))
activity_kb.tell(expr('Age(Adult, x)==>Age(Over10, x)'))
activity_kb.tell(expr('Age(Young, x)==>Age(Over33, x)'))
activity_kb.tell(expr('Age(Teen, x)==>Age(Over33, x)'))

activity_kb.tell(expr('SocialInteraction(Alone, x) ==> SocialInteraction(NoMatter, x)'))
activity_kb.tell(expr('SocialInteraction(Group, x) ==> SocialInteraction(NoMatter, x)'))

activity_kb.tell(expr('MaterialNeeded(Expensive, x)==>MaterialNeeded(Moderate, x)'))
activity_kb.tell(expr('MaterialNeeded(Moderate, x)==>MaterialNeeded(Minimal, x)'))

activity_kb.tell(expr('MoneySpendingByMounth(VeryExpensive, x)==>MoneySpendingByMounth(Expensive, x)'))
activity_kb.tell(expr('MoneySpendingByMounth(Expensive, x)==>MoneySpendingByMounth(Moderate, x)'))
activity_kb.tell(expr('MoneySpendingByMounth(Moderate, x)==>MoneySpendingByMounth(Free, x)'))

activity_kb.tell(expr('Place(Interior, x)==>Place(Whatever, x)'))
activity_kb.tell(expr('Place(Exterior, x)==>Place(Whatever, x)'))

activity_kb.tell(expr('ActivityType(Mental, x)&Dev(Brain, x)==>Type(Logical, x)'))
activity_kb.tell(expr('ActivityType(Mental, x)&Dev(Soul, x)==>Type(Art, x)'))
activity_kb.tell(expr('ActivityType(Physical, x)&Dev(Soul, x)==>Type(Strength, x)'))
activity_kb.tell(expr('ActivityType(Physical, x)&Dev(Brain, x)==>Type(Flexibility, x)'))

activity_kb.tell(expr('ActivityType(Physical, x)&Dev(Soul, x)==>Type(Strength, x)'))

# Chess
activity_kb.tell(expr('Type(Logical, x)&Place(Interior, x)&SocialInteraction(Alone, x)&GoalTime(Long, x)&MoneySpendingByMounth(Free, x)&MaterialNeeded(Minimal, x)==>Activity(Chess, x)'))

# Football
activity_kb.tell(expr('SocialInteraction(Group, x)&Safety(NoMatter, x)&GoalTime(Long, x)&Age(Young, x)&MoneySpendingByMounth(Expensive, x)==>Activity(Football, x)'))

# Yoga
activity_kb.tell(expr('GoalTime(Long, x)&MaterialNeeded(Moderate, x)==>Activity(Yoga, x)'))

# Sudoku
activity_kb.tell(expr('GoalTime(Short, x)&Type(Logical, x)==>Activity(Sudoku, x)'))
activity_kb.tell(expr('Type(Logical, x)&Place(Interior, x)&MoneySpendingByMounth(Free, x)&MaterialNeeded(Minimal, x)==>Activity(Sudoku, x)'))

# Music
activity_kb.tell(expr('Type(Art, x)&GoalTime(Long, x)==>Activity(Music, x)'))

# Dance
activity_kb.tell(expr('Type(Art, x)&ActivityType(Physical, x)==>Activity(Dance, x)'))

# Painting
activity_kb.tell(expr('Type(Art, x)&Place(Whatever, x)==>Activity(Painting, x)'))

# Rock Climbing
activity_kb.tell(expr('Type(Strength, x)&Place(Exterior, x)==>Activity(Rock_Climbing, x)'))

# Crossword Puzzles
activity_kb.tell(expr('Type(Logical, x)&SocialInteraction(Alone, x)==>Activity(Crossword_Puzzles, x)'))
activity_kb.tell(expr('Type(Logical, x)&Place(Interior, x)==>Activity(Crossword_Puzzles, x)'))

# Hiking
activity_kb.tell(expr('Place(Exterior, x)&MaterialNeeded(Expensive, x)&ActivityType(Physical, x)&SocialInteraction(Group, x)==>Activity(Hiking, x)'))

# Photography
activity_kb.tell(expr('Place(Exterior, x)&MaterialNeeded(VeryExpensive, x)&SocialInteraction(NoMatter, x)==>Activity(Photography, x)'))

# Martial Arts
activity_kb.tell(expr('Type(Strength, x) ==> Activity(Martial_Arts, x)'))

# Swimming
activity_kb.tell(expr('Type(Strength, x)&MoneySpendingByMounth(Moderate, x) ==>Activity(Swimming, x)'))

# Cooking
activity_kb.tell(expr('Place(Internal, x)&MoneySpendingByMounth(VeryExpensive, x)&ActivityType(Mental, x)==>Activity(Cooking, x)'))

# Cycling
activity_kb.tell(expr('Type(Flexibility, x)&MaterialNeeded(Expensive, x)&SocialInteraction(NoMatter, x)==>Activity(Cycling, x)'))

# Language Learning
activity_kb.tell(expr('ActivityType(Mental, x) & MoneySpendingByMounth(Free, x) & GoalTime(Long, x)  ==> Activity(Language_Learning, x)'))