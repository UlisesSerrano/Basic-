from collections import defaultdict

semantic_cube = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

semantic_cube['int']['+']['int'] = 'int'
semantic_cube['int']['-']['int'] = 'int'
semantic_cube['int']['*']['int'] = 'int'
semantic_cube['int']['/']['int'] = 'int'
semantic_cube['int']['=']['int'] = 'int'
semantic_cube['int']['%']['int'] = 'int'

semantic_cube['int']['>']['int'] = 'int'
semantic_cube['int']['<']['int'] = 'int'
semantic_cube['int']['>=']['int'] = 'int'
semantic_cube['int']['<=']['int'] = 'int'
semantic_cube['int']['==']['int'] = 'int'
semantic_cube['int']['!=']['int'] = 'int'

semantic_cube['int']['+']['float'] = 'float'
semantic_cube['int']['-']['float'] = 'float'
semantic_cube['int']['*']['float'] = 'float'
semantic_cube['int']['/']['float'] = 'float'
semantic_cube['int']['=']['float'] = 'float'
semantic_cube['int']['%']['float'] = 'float'

semantic_cube['int']['>']['float'] = 'int'
semantic_cube['int']['<']['float'] = 'int'
semantic_cube['int']['>=']['float'] = 'int'
semantic_cube['int']['<=']['float'] = 'int'
semantic_cube['int']['==']['float'] = 'int'
semantic_cube['int']['!=']['float'] = 'int'

semantic_cube['float']['+']['int'] = 'float'
semantic_cube['float']['-']['int'] = 'float'
semantic_cube['float']['*']['int'] = 'float'
semantic_cube['float']['/']['int'] = 'float'
semantic_cube['float']['=']['int'] = 'float'
semantic_cube['float']['%']['int'] = 'float'

semantic_cube['float']['>']['int'] = 'int'
semantic_cube['float']['<']['int'] = 'int'
semantic_cube['float']['>=']['int'] = 'int'
semantic_cube['float']['<=']['int'] = 'int'
semantic_cube['float']['==']['int'] = 'int'
semantic_cube['float']['!=']['int'] = 'int'

semantic_cube['float']['+']['float'] = 'float'
semantic_cube['float']['-']['float'] = 'float'
semantic_cube['float']['*']['float'] = 'float'
semantic_cube['float']['/']['float'] = 'float'
semantic_cube['float']['=']['float'] = 'float'
semantic_cube['float']['%']['float'] = 'float'

semantic_cube['float']['>']['float'] = 'int'
semantic_cube['float']['<']['float'] = 'int'
semantic_cube['float']['>=']['float'] = 'int'
semantic_cube['float']['<=']['float'] = 'int'
semantic_cube['float']['==']['float'] = 'int'
semantic_cube['float']['!=']['float'] = 'int'

semantic_cube['char']['=']['char'] = 'char'
semantic_cube['char']['==']['char'] = 'int'
semantic_cube['char']['!=']['char'] = 'int'

emantic_cube['int']['&']['int'] = 'int'
semantic_cube['int']['|']['int'] = 'int' 


