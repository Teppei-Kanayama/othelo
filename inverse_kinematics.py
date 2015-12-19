#!/usr/bin/env python
# -*- coding : utf-8 -*-

import numpy as np

base_arg = np.zeros([6, 6])
end_arg = np.zeros([6, 6])

base_arg[0][0] =60
base_arg[0][1] =60
base_arg[0][2] =60
base_arg[0][3] =60
base_arg[0][4] =120
base_arg[0][5] =60

base_arg[1][0] =60
base_arg[1][1] =60
base_arg[1][2] =135
base_arg[1][3] =135
base_arg[1][4] =130
base_arg[1][5] =120

base_arg[2][0] =150
base_arg[2][1] =150
base_arg[2][2] =150
base_arg[2][3] =145
base_arg[2][4] =130
base_arg[2][5] =120

base_arg[3][0] =165
base_arg[3][1] =160
base_arg[3][2] =160
base_arg[3][3] =150
base_arg[3][4] =140
base_arg[3][5] =130

base_arg[4][0] =175
base_arg[4][1] =170
base_arg[4][2] =160
base_arg[4][3] =150
base_arg[4][4] =140
base_arg[4][5] =130

base_arg[5][0] =180
base_arg[5][1] =180
base_arg[5][2] =170
base_arg[5][3] =160
base_arg[5][4] =150
base_arg[5][5] =135

end_arg[0][0] =60
end_arg[0][1] =60
end_arg[0][2] =60
end_arg[0][3] =60
end_arg[0][4] =60
end_arg[0][5] =60

end_arg[1][0] =60
end_arg[1][1] =60
end_arg[1][2] =65
end_arg[1][3] =80
end_arg[1][4] =80
end_arg[1][5] =70

end_arg[2][0] =70
end_arg[2][1] =80
end_arg[2][2] =90
end_arg[2][3] =95
end_arg[2][4] =90
end_arg[2][5] =85

end_arg[3][0] =85
end_arg[3][1] =100
end_arg[3][2] =105
end_arg[3][3] =105
end_arg[3][4] =105
end_arg[3][5] =105

end_arg[4][0] =100
end_arg[4][1] =110
end_arg[4][2] =115
end_arg[4][3] =115
end_arg[4][4] =115
end_arg[4][5] =110

end_arg[5][0] =110
end_arg[5][1] =120
end_arg[5][2] =130
end_arg[5][3] =130
end_arg[5][4] =130
end_arg[5][5] =130

def pos_to_arg(pos):
    return [base_arg[pos[0]][pos[1]], end_arg[pos[0]][pos[1]]]
