#!/usr/bin/env python
# -*- coding : utf-8 -*-

import numpy as np

base_arg = np.zeros([8, 8])
end_arg = np.zeros([8, 8])

base_arg[0][0] =60
base_arg[0][1] =60
base_arg[0][2] =60
base_arg[0][3] =60
base_arg[0][4] =60
base_arg[0][5] =60
base_arg[0][6] =60
base_arg[0][7] =60

base_arg[1][0] =60
base_arg[1][1] =60
base_arg[1][2] =60
base_arg[1][3] =60
base_arg[1][4] =60
base_arg[1][5] =60
base_arg[1][6] =60
base_arg[1][7] =60

base_arg[2][0] =60
base_arg[2][1] =60
base_arg[2][2] =60
base_arg[2][3] =60
base_arg[2][4] =60
base_arg[2][5] =60
base_arg[2][6] =60
base_arg[2][7] =60

base_arg[3][0] =60
base_arg[3][1] =60
base_arg[3][2] =60
base_arg[3][3] =60
base_arg[3][4] =60
base_arg[3][5] =60
base_arg[3][6] =60
base_arg[3][7] =60

base_arg[4][0] =60
base_arg[4][1] =60
base_arg[4][2] =60
base_arg[4][3] =60
base_arg[4][4] =60
base_arg[4][5] =60
base_arg[4][6] =60
base_arg[4][7] =60

base_arg[5][0] =60
base_arg[5][1] =60
base_arg[5][2] =60
base_arg[5][3] =60
base_arg[5][4] =60
base_arg[5][5] =60
base_arg[5][6] =60
base_arg[5][7] =60

base_arg[6][0] =60
base_arg[6][1] =60
base_arg[6][2] =60
base_arg[6][3] =60
base_arg[6][4] =60
base_arg[6][5] =60
base_arg[6][6] =60
base_arg[6][7] =60

base_arg[7][0] =60
base_arg[7][1] =60
base_arg[7][2] =60
base_arg[7][3] =60
base_arg[7][4] =60
base_arg[7][5] =60
base_arg[7][6] =60
base_arg[7][7] =60



end_arg[0][0] =60
end_arg[0][1] =60
end_arg[0][2] =60
end_arg[0][3] =60
end_arg[0][4] =60
end_arg[0][5] =60
end_arg[0][6] =60
end_arg[0][7] =60

end_arg[1][0] =60
end_arg[1][1] =60
end_arg[1][2] =60
end_arg[1][3] =60
end_arg[1][4] =60
end_arg[1][5] =60
end_arg[1][6] =60
end_arg[1][7] =60

end_arg[2][0] =60
end_arg[2][1] =60
end_arg[2][2] =60
end_arg[2][3] =60
end_arg[2][4] =60
end_arg[2][5] =60
end_arg[2][6] =60
end_arg[2][7] =60

end_arg[3][0] =60
end_arg[3][1] =60
end_arg[3][2] =60
end_arg[3][3] =60
end_arg[3][4] =60
end_arg[3][5] =60
end_arg[3][6] =60
end_arg[3][7] =60

end_arg[4][0] =60
end_arg[4][1] =60
end_arg[4][2] =60
end_arg[4][3] =60
end_arg[4][4] =60
end_arg[4][5] =60
end_arg[4][6] =60
end_arg[4][7] =60

end_arg[5][0] =60
end_arg[5][1] =60
end_arg[5][2] =60
end_arg[5][3] =60
end_arg[5][4] =60
end_arg[5][5] =60
end_arg[5][6] =60
end_arg[5][7] =60

end_arg[6][0] =60
end_arg[6][1] =60
end_arg[6][2] =60
end_arg[6][3] =60
end_arg[6][4] =60
end_arg[6][5] =60
end_arg[6][6] =60
end_arg[6][7] =60

end_arg[7][0] =60
end_arg[7][1] =60
end_arg[7][2] =60
end_arg[7][3] =60
end_arg[7][4] =60
end_arg[7][5] =60
end_arg[7][6] =60
end_arg[7][7] =60

def pos_to_arg(pos):
    return [base_arg[pos[0]][pos[1]], end_arg[pos[0]][pos[1]]]
