"""
Write a Python function number_of_collisions(objects) that returns the amount of collisions between each object given in the list objects.
""" 

def number_of_collisions(objects):
    collisions = 0
    combs = []
    for i in range(len(objects)):
        for j in range(i+1, len(objects)):
            if (objects[i], objects[j]) not in combs:
                combs.append((objects[i], objects[j]))
                if objects[i]['x2'] >= objects[j]['x1'] and objects[i]['x1'] <= objects[j]['x2'] and objects[i]['y2'] >= objects[j]['y1'] and objects[i]['y1'] <= objects[j]['y2']:
                    collisions += 1
    return collisions


print(number_of_collisions([{'x1': 11, 'y1': 192, 'x2': 59, 'y2': 280}, {'x1': 546, 'y1': 564, 'x2': 629, 'y2': 580}, {'x1': 368, 'y1': 418, 'x2': 455, 'y2': 432}, {'x1': 479, 'y1': 506, 'x2': 577, 'y2': 521}, {'x1': 113, 'y1': 315, 'x2': 156, 'y2': 415}, {'x1': 513, 'y1': 40, 'x2': 537, 'y2': 119}, {'x1': 521, 'y1': 488, 'x2': 549, 'y2': 522}, {'x1': 72, 'y1': 295, 'x2': 122, 'y2': 343}, {'x1': 87, 'y1': 160, 'x2': 135, 'y2': 213}, {'x1': 495, 'y1': 304, 'x2': 524, 'y2': 339}]))
print(number_of_collisions([{'x1': 0, 'y1': 0, 'x2': 2, 'y2': 2}, {'x1': 3, 'y1': 3, 'x2': 5, 'y2': 5}]))
print(number_of_collisions([{'x1': 37, 'y1': 560, 'x2': 48, 'y2': 634}, {'x1': 456, 'y1': 391, 'x2': 539, 'y2': 404}, {'x1': 407, 'y1': 536, 'x2': 468, 'y2': 589}, {'x1': 538, 'y1': 500, 'x2': 633, 'y2': 573}, {'x1': 343, 'y1': 584, 'x2': 407, 'y2': 606}, {'x1': 334, 'y1': 177, 'x2': 371, 'y2': 220}, {'x1': 239, 'y1': 111, 'x2': 325, 'y2': 159}, {'x1': 512, 'y1': 343, 'x2': 540, 'y2': 356}, {'x1': 544, 'y1': 341, 'x2': 578, 'y2': 439}, {'x1': 33, 'y1': 143, 'x2': 57, 'y2': 237}, {'x1': 200, 'y1': 403, 'x2': 260, 'y2': 458}, {'x1': 454, 'y1': 102, 'x2': 516, 'y2': 160}, {'x1': 522, 'y1': 59, 'x2': 578, 'y2': 133}, {'x1': 68, 'y1': 546, 'x2': 112, 'y2': 594}, {'x1': 251, 'y1': 354, 'x2': 268, 'y2': 390}, {'x1': 234, 'y1': 564, 'x2': 260, 'y2': 619}, {'x1': 130, 'y1': 473, 'x2': 163, 'y2': 507}, {'x1': 556, 'y1': 225, 'x2': 630, 'y2': 287}, {'x1': 181, 'y1': 145, 'x2': 232, 'y2': 234}, {'x1': 455, 'y1': 122, 'x2': 516, 'y2': 154}, {'x1': 490, 'y1': 359, 'x2': 545, 'y2': 422}, {'x1': 514, 'y1': 503, 'x2': 613, 'y2': 520}, {'x1': 264, 'y1': 470, 'x2': 290, 'y2': 518}, {'x1': 146, 'y1': 262, 'x2': 157, 'y2': 320}, {'x1': 117, 'y1': 503, 'x2': 155, 'y2': 515}, {'x1': 52, 'y1': 280, 'x2': 91, 'y2': 348}, {'x1': 119, 'y1': 99, 'x2': 191, 'y2': 192}, {'x1': 554, 'y1': 588, 'x2': 636, 'y2': 658}, {'x1': 441, 'y1': 287, 'x2': 478, 'y2': 332}, {'x1': 123, 'y1': 60, 'x2': 185, 'y2': 118}, {'x1': 440, 'y1': 193, 'x2': 484, 'y2': 260}, {'x1': 232, 'y1': 136, 'x2': 248, 'y2': 187}, {'x1': 96, 'y1': 225, 'x2': 174, 'y2': 301}, {'x1': 291, 'y1': 27, 'x2': 311, 'y2': 75}, {'x1': 247, 'y1': 348, 'x2': 257, 'y2': 438}, {'x1': 491, 'y1': 548, 'x2': 570, 'y2': 613}, {'x1': 375, 'y1': 100, 'x2': 420, 'y2': 152}, {'x1': 375, 'y1': 235, 'x2': 398, 'y2': 256}, {'x1': 272, 'y1': 451, 'x2': 294, 'y2': 484}, {'x1': 248, 'y1': 480, 'x2': 342, 'y2': 578}, {'x1': 331, 'y1': 445, 'x2': 406, 'y2': 502}, {'x1': 243, 'y1': 35, 'x2': 322, 'y2': 69}, {'x1': 14, 'y1': 165, 'x2': 98, 'y2': 229}, {'x1': 425, 'y1': 556, 'x2': 464, 'y2': 648}, {'x1': 82, 'y1': 46, 'x2': 162, 'y2': 100}, {'x1': 482, 'y1': 65, 'x2': 532, 'y2': 129}, {'x1': 254, 'y1': 1, 'x2': 329, 'y2': 77}, {'x1': 431, 'y1': 471, 'x2': 504, 'y2': 525}, {'x1': 242, 'y1': 169, 'x2': 306, 'y2': 225}, {'x1': 400, 'y1': 484, 'x2': 420, 'y2': 578}, {'x1': 167, 'y1': 464, 'x2': 246, 'y2': 485}, {'x1': 416, 'y1': 479, 'x2': 443, 'y2': 500}, {'x1': 272, 'y1': 281, 'x2': 358, 'y2': 313}, {'x1': 357, 'y1': 10, 'x2': 444, 'y2': 30}, {'x1': 337, 'y1': 55, 'x2': 421, 'y2': 137}, {'x1': 555, 'y1': 588, 'x2': 624, 'y2': 668}, {'x1': 330, 'y1': 213, 'x2': 395, 'y2': 280}, {'x1': 452, 'y1': 332, 'x2': 540, 'y2': 391}, {'x1': 265, 'y1': 491, 'x2': 301, 'y2': 573}, {'x1': 433, 'y1': 256, 'x2': 450, 'y2': 297}, {'x1': 309, 'y1': 212, 'x2': 376, 'y2': 268}, {'x1': 435, 'y1': 113, 'x2': 467, 'y2': 186}, {'x1': 406, 'y1': 584, 'x2': 420, 'y2': 632}, {'x1': 37, 'y1': 72, 'x2': 137, 'y2': 137}, {'x1': 101, 'y1': 465, 'x2': 191, 'y2': 541}, {'x1': 591, 'y1': 432, 'x2': 644, 'y2': 457}, {'x1': 419, 'y1': 330, 'x2': 481, 'y2': 425}, {'x1': 437, 'y1': 314, 'x2': 475, 'y2': 346}, {'x1': 156, 'y1': 453, 'x2': 176, 'y2': 524}, {'x1': 16, 'y1': 285, 'x2': 90, 'y2': 348}, {'x1': 75, 'y1': 353, 'x2': 94, 'y2': 441}, {'x1': 55, 'y1': 81, 'x2': 72, 'y2': 112}, {'x1': 520, 'y1': 152, 'x2': 544, 'y2': 162}, {'x1': 139, 'y1': 577, 'x2': 225, 'y2': 624}, {'x1': 415, 'y1': 364, 'x2': 438, 'y2': 445}, {'x1': 406, 'y1': 387, 'x2': 459, 'y2': 428}, {'x1': 317, 'y1': 77, 'x2': 390, 'y2': 107}, {'x1': 390, 'y1': 282, 'x2': 439, 'y2': 338}, {'x1': 380, 'y1': 10, 'x2': 460, 'y2': 69}, {'x1': 261, 'y1': 358, 'x2': 336, 'y2': 452}, {'x1': 132, 'y1': 482, 'x2': 214, 'y2': 507}, {'x1': 167, 'y1': 432, 'x2': 250, 'y2': 473}, {'x1': 45, 'y1': 550, 'x2': 137, 'y2': 603}, {'x1': 265, 'y1': 278, 'x2': 315, 'y2': 312}, {'x1': 207, 'y1': 517, 'x2': 227, 'y2': 571}, {'x1': 303, 'y1': 286, 'x2': 320, 'y2': 350}, {'x1': 406, 'y1': 214, 'x2': 493, 'y2': 277}, {'x1': 532, 'y1': 325, 'x2': 549, 'y2': 391}, {'x1': 337, 'y1': 158, 'x2': 355, 'y2': 210}, {'x1': 25, 'y1': 482, 'x2': 53, 'y2': 561}, {'x1': 255, 'y1': 62, 'x2': 317, 'y2': 160}, {'x1': 215, 'y1': 190, 'x2': 284, 'y2': 284}, {'x1': 93, 'y1': 495, 'x2': 185, 'y2': 547}, {'x1': 500, 'y1': 46, 'x2': 539, 'y2': 99}, {'x1': 405, 'y1': 256, 'x2': 481, 'y2': 273}, {'x1': 361, 'y1': 416, 'x2': 419, 'y2': 477}, {'x1': 203, 'y1': 486, 'x2': 237, 'y2': 574}, {'x1': 356, 'y1': 137, 'x2': 415, 'y2': 230}, {'x1': 240, 'y1': 466, 'x2': 252, 'y2': 501}, {'x1': 203, 'y1': 418, 'x2': 289, 'y2': 440}]))
print(number_of_collisions([{'x1': 44, 'y1': 111, 'x2': 62, 'y2': 177}, {'x1': 85, 'y1': 82, 'x2': 130, 'y2': 134}, {'x1': 3, 'y1': 181, 'x2': 26, 'y2': 272}, {'x1': 262, 'y1': 95, 'x2': 291, 'y2': 117}, {'x1': 321, 'y1': 75, 'x2': 366, 'y2': 95}, {'x1': 280, 'y1': 570, 'x2': 368, 'y2': 662}, {'x1': 36, 'y1': 462, 'x2': 125, 'y2': 506}, {'x1': 396, 'y1': 105, 'x2': 487, 'y2': 133}, {'x1': 224, 'y1': 106, 'x2': 261, 'y2': 151}, {'x1': 104, 'y1': 450, 'x2': 187, 'y2': 489}, {'x1': 91, 'y1': 381, 'x2': 106, 'y2': 434}, {'x1': 34, 'y1': 588, 'x2': 71, 'y2': 680}, {'x1': 213, 'y1': 90, 'x2': 298, 'y2': 172}, {'x1': 497, 'y1': 514, 'x2': 570, 'y2': 543}, {'x1': 330, 'y1': 243, 'x2': 376, 'y2': 296}, {'x1': 15, 'y1': 583, 'x2': 87, 'y2': 663}, {'x1': 17, 'y1': 469, 'x2': 49, 'y2': 508}, {'x1': 357, 'y1': 94, 'x2': 378, 'y2': 129}, {'x1': 15, 'y1': 551, 'x2': 29, 'y2': 587}, {'x1': 226, 'y1': 334, 'x2': 297, 'y2': 381}, {'x1': 324, 'y1': 20, 'x2': 363, 'y2': 86}, {'x1': 504, 'y1': 500, 'x2': 598, 'y2': 560}, {'x1': 113, 'y1': 506, 'x2': 131, 'y2': 535}, {'x1': 194, 'y1': 310, 'x2': 260, 'y2': 329}, {'x1': 560, 'y1': 338, 'x2': 580, 'y2': 365}, {'x1': 413, 'y1': 255, 'x2': 491, 'y2': 326}, {'x1': 380, 'y1': 285, 'x2': 463, 'y2': 369}, {'x1': 556, 'y1': 260, 'x2': 579, 'y2': 357}, {'x1': 291, 'y1': 7, 'x2': 380, 'y2': 61}, {'x1': 361, 'y1': 0, 'x2': 433, 'y2': 22}, {'x1': 544, 'y1': 548, 'x2': 586, 'y2': 626}, {'x1': 447, 'y1': 150, 'x2': 543, 'y2': 211}, {'x1': 99, 'y1': 288, 'x2': 186, 'y2': 325}, {'x1': 594, 'y1': 430, 'x2': 617, 'y2': 488}, {'x1': 469, 'y1': 7, 'x2': 546, 'y2': 67}, {'x1': 45, 'y1': 143, 'x2': 143, 'y2': 188}, {'x1': 580, 'y1': 118, 'x2': 608, 'y2': 182}, {'x1': 11, 'y1': 245, 'x2': 24, 'y2': 342}, {'x1': 187, 'y1': 303, 'x2': 208, 'y2': 394}, {'x1': 175, 'y1': 272, 'x2': 264, 'y2': 311}, {'x1': 272, 'y1': 162, 'x2': 303, 'y2': 180}, {'x1': 109, 'y1': 57, 'x2': 203, 'y2': 156}, {'x1': 350, 'y1': 119, 'x2': 434, 'y2': 207}, {'x1': 104, 'y1': 533, 'x2': 159, 'y2': 615}, {'x1': 239, 'y1': 257, 'x2': 303, 'y2': 327}, {'x1': 60, 'y1': 347, 'x2': 91, 'y2': 357}, {'x1': 372, 'y1': 529, 'x2': 391, 'y2': 626}, {'x1': 186, 'y1': 55, 'x2': 219, 'y2': 104}, {'x1': 542, 'y1': 425, 'x2': 595, 'y2': 459}, {'x1': 547, 'y1': 36, 'x2': 558, 'y2': 80}, {'x1': 409, 'y1': 382, 'x2': 467, 'y2': 418}, {'x1': 309, 'y1': 452, 'x2': 348, 'y2': 478}, {'x1': 487, 'y1': 14, 'x2': 585, 'y2': 105}, {'x1': 309, 'y1': 442, 'x2': 344, 'y2': 537}, {'x1': 399, 'y1': 555, 'x2': 420, 'y2': 601}, {'x1': 38, 'y1': 169, 'x2': 109, 'y2': 239}, {'x1': 414, 'y1': 172, 'x2': 472, 'y2': 236}, {'x1': 323, 'y1': 383, 'x2': 363, 'y2': 401}, {'x1': 117, 'y1': 197, 'x2': 128, 'y2': 228}, {'x1': 411, 'y1': 220, 'x2': 462, 'y2': 306}, {'x1': 327, 'y1': 32, 'x2': 373, 'y2': 116}, {'x1': 174, 'y1': 445, 'x2': 202, 'y2': 496}, {'x1': 83, 'y1': 469, 'x2': 133, 'y2': 487}, {'x1': 39, 'y1': 23, 'x2': 90, 'y2': 64}, {'x1': 114, 'y1': 545, 'x2': 129, 'y2': 606}, {'x1': 16, 'y1': 108, 'x2': 27, 'y2': 156}, {'x1': 430, 'y1': 524, 'x2': 529, 'y2': 561}, {'x1': 289, 'y1': 399, 'x2': 322, 'y2': 419}, {'x1': 51, 'y1': 459, 'x2': 102, 'y2': 521}, {'x1': 420, 'y1': 396, 'x2': 446, 'y2': 484}, {'x1': 324, 'y1': 248, 'x2': 335, 'y2': 288}, {'x1': 51, 'y1': 307, 'x2': 123, 'y2': 319}, {'x1': 359, 'y1': 288, 'x2': 374, 'y2': 299}, {'x1': 48, 'y1': 201, 'x2': 95, 'y2': 277}, {'x1': 583, 'y1': 501, 'x2': 667, 'y2': 555}, {'x1': 466, 'y1': 121, 'x2': 517, 'y2': 166}, {'x1': 165, 'y1': 270, 'x2': 255, 'y2': 360}, {'x1': 30, 'y1': 416, 'x2': 108, 'y2': 437}, {'x1': 542, 'y1': 411, 'x2': 566, 'y2': 505}, {'x1': 159, 'y1': 448, 'x2': 175, 'y2': 502}, {'x1': 26, 'y1': 349, 'x2': 39, 'y2': 424}, {'x1': 588, 'y1': 593, 'x2': 674, 'y2': 630}, {'x1': 360, 'y1': 508, 'x2': 448, 'y2': 572}, {'x1': 312, 'y1': 384, 'x2': 409, 'y2': 413}, {'x1': 513, 'y1': 351, 'x2': 576, 'y2': 381}, {'x1': 131, 'y1': 599, 'x2': 200, 'y2': 650}, {'x1': 396, 'y1': 163, 'x2': 406, 'y2': 209}, {'x1': 538, 'y1': 238, 'x2': 551, 'y2': 302}, {'x1': 62, 'y1': 81, 'x2': 109, 'y2': 174}, {'x1': 327, 'y1': 139, 'x2': 355, 'y2': 213}, {'x1': 217, 'y1': 340, 'x2': 241, 'y2': 382}, {'x1': 297, 'y1': 293, 'x2': 347, 'y2': 328}, {'x1': 259, 'y1': 9, 'x2': 294, 'y2': 76}, {'x1': 248, 'y1': 342, 'x2': 304, 'y2': 420}, {'x1': 179, 'y1': 507, 'x2': 218, 'y2': 565}, {'x1': 491, 'y1': 269, 'x2': 533, 'y2': 299}, {'x1': 297, 'y1': 385, 'x2': 339, 'y2': 480}, {'x1': 334, 'y1': 140, 'x2': 426, 'y2': 169}, {'x1': 429, 'y1': 445, 'x2': 516, 'y2': 492}, {'x1': 4, 'y1': 472, 'x2': 40, 'y2': 512}]))
print(number_of_collisions([{'x1': 525, 'y1': 273, 'x2': 608, 'y2': 316}, {'x1': 99, 'y1': 385, 'x2': 198, 'y2': 440}, {'x1': 426, 'y1': 224, 'x2': 442, 'y2': 310}, {'x1': 109, 'y1': 275, 'x2': 190, 'y2': 306}, {'x1': 143, 'y1': 290, 'x2': 164, 'y2': 350}, {'x1': 138, 'y1': 293, 'x2': 229, 'y2': 308}, {'x1': 548, 'y1': 170, 'x2': 624, 'y2': 250}, {'x1': 101, 'y1': 318, 'x2': 168, 'y2': 338}, {'x1': 378, 'y1': 215, 'x2': 460, 'y2': 275}, {'x1': 62, 'y1': 596, 'x2': 133, 'y2': 613}, {'x1': 265, 'y1': 459, 'x2': 281, 'y2': 548}, {'x1': 162, 'y1': 145, 'x2': 229, 'y2': 191}, {'x1': 179, 'y1': 440, 'x2': 266, 'y2': 496}, {'x1': 31, 'y1': 486, 'x2': 81, 'y2': 532}, {'x1': 287, 'y1': 109, 'x2': 369, 'y2': 155}, {'x1': 548, 'y1': 20, 'x2': 619, 'y2': 107}, {'x1': 375, 'y1': 125, 'x2': 409, 'y2': 179}, {'x1': 378, 'y1': 500, 'x2': 425, 'y2': 511}, {'x1': 175, 'y1': 303, 'x2': 248, 'y2': 357}, {'x1': 140, 'y1': 515, 'x2': 210, 'y2': 540}, {'x1': 312, 'y1': 71, 'x2': 367, 'y2': 129}, {'x1': 270, 'y1': 487, 'x2': 296, 'y2': 497}, {'x1': 334, 'y1': 381, 'x2': 416, 'y2': 459}, {'x1': 223, 'y1': 552, 'x2': 253, 'y2': 638}, {'x1': 9, 'y1': 365, 'x2': 51, 'y2': 394}, {'x1': 400, 'y1': 420, 'x2': 444, 'y2': 497}, {'x1': 106, 'y1': 397, 'x2': 182, 'y2': 442}, {'x1': 265, 'y1': 536, 'x2': 320, 'y2': 622}, {'x1': 61, 'y1': 64, 'x2': 89, 'y2': 131}, {'x1': 74, 'y1': 298, 'x2': 90, 'y2': 382}, {'x1': 364, 'y1': 40, 'x2': 402, 'y2': 59}, {'x1': 65, 'y1': 143, 'x2': 113, 'y2': 197}, {'x1': 185, 'y1': 121, 'x2': 220, 'y2': 167}, {'x1': 185, 'y1': 504, 'x2': 232, 'y2': 529}, {'x1': 321, 'y1': 582, 'x2': 389, 'y2': 651}, {'x1': 203, 'y1': 562, 'x2': 248, 'y2': 638}, {'x1': 344, 'y1': 369, 'x2': 419, 'y2': 462}, {'x1': 124, 'y1': 29, 'x2': 204, 'y2': 63}, {'x1': 338, 'y1': 113, 'x2': 378, 'y2': 202}, {'x1': 179, 'y1': 263, 'x2': 259, 'y2': 332}, {'x1': 144, 'y1': 590, 'x2': 156, 'y2': 602}, {'x1': 586, 'y1': 472, 'x2': 675, 'y2': 484}, {'x1': 347, 'y1': 264, 'x2': 437, 'y2': 293}, {'x1': 410, 'y1': 230, 'x2': 457, 'y2': 254}, {'x1': 518, 'y1': 99, 'x2': 543, 'y2': 148}, {'x1': 164, 'y1': 338, 'x2': 258, 'y2': 379}, {'x1': 301, 'y1': 405, 'x2': 327, 'y2': 428}, {'x1': 151, 'y1': 174, 'x2': 243, 'y2': 186}, {'x1': 134, 'y1': 141, 'x2': 196, 'y2': 240}, {'x1': 580, 'y1': 275, 'x2': 621, 'y2': 309}, {'x1': 189, 'y1': 444, 'x2': 257, 'y2': 500}, {'x1': 389, 'y1': 90, 'x2': 464, 'y2': 169}, {'x1': 525, 'y1': 197, 'x2': 583, 'y2': 233}, {'x1': 197, 'y1': 422, 'x2': 286, 'y2': 503}, {'x1': 546, 'y1': 476, 'x2': 565, 'y2': 546}, {'x1': 461, 'y1': 423, 'x2': 479, 'y2': 463}, {'x1': 340, 'y1': 249, 'x2': 416, 'y2': 308}, {'x1': 41, 'y1': 450, 'x2': 58, 'y2': 497}, {'x1': 555, 'y1': 308, 'x2': 641, 'y2': 366}, {'x1': 66, 'y1': 29, 'x2': 83, 'y2': 40}, {'x1': 343, 'y1': 176, 'x2': 412, 'y2': 210}, {'x1': 57, 'y1': 444, 'x2': 147, 'y2': 478}, {'x1': 132, 'y1': 155, 'x2': 224, 'y2': 181}, {'x1': 156, 'y1': 240, 'x2': 176, 'y2': 328}, {'x1': 492, 'y1': 553, 'x2': 502, 'y2': 600}, {'x1': 184, 'y1': 259, 'x2': 266, 'y2': 324}, {'x1': 539, 'y1': 449, 'x2': 580, 'y2': 496}, {'x1': 465, 'y1': 39, 'x2': 546, 'y2': 64}, {'x1': 501, 'y1': 599, 'x2': 601, 'y2': 693}, {'x1': 494, 'y1': 125, 'x2': 530, 'y2': 170}, {'x1': 204, 'y1': 268, 'x2': 258, 'y2': 362}, {'x1': 17, 'y1': 227, 'x2': 27, 'y2': 307}, {'x1': 51, 'y1': 39, 'x2': 87, 'y2': 63}, {'x1': 391, 'y1': 403, 'x2': 409, 'y2': 480}, {'x1': 65, 'y1': 403, 'x2': 90, 'y2': 423}, {'x1': 28, 'y1': 383, 'x2': 68, 'y2': 473}, {'x1': 149, 'y1': 355, 'x2': 178, 'y2': 455}, {'x1': 236, 'y1': 277, 'x2': 310, 'y2': 360}, {'x1': 147, 'y1': 600, 'x2': 174, 'y2': 672}, {'x1': 51, 'y1': 466, 'x2': 104, 'y2': 524}, {'x1': 456, 'y1': 118, 'x2': 552, 'y2': 207}, {'x1': 174, 'y1': 492, 'x2': 226, 'y2': 530}, {'x1': 142, 'y1': 596, 'x2': 226, 'y2': 612}, {'x1': 329, 'y1': 269, 'x2': 398, 'y2': 314}, {'x1': 31, 'y1': 141, 'x2': 119, 'y2': 227}, {'x1': 278, 'y1': 67, 'x2': 299, 'y2': 87}, {'x1': 441, 'y1': 348, 'x2': 463, 'y2': 374}, {'x1': 136, 'y1': 378, 'x2': 172, 'y2': 409}, {'x1': 184, 'y1': 117, 'x2': 254, 'y2': 138}, {'x1': 433, 'y1': 132, 'x2': 514, 'y2': 210}, {'x1': 435, 'y1': 184, 'x2': 506, 'y2': 232}, {'x1': 51, 'y1': 290, 'x2': 62, 'y2': 353}, {'x1': 480, 'y1': 241, 'x2': 533, 'y2': 261}, {'x1': 596, 'y1': 333, 'x2': 613, 'y2': 385}, {'x1': 281, 'y1': 235, 'x2': 336, 'y2': 329}, {'x1': 3, 'y1': 497, 'x2': 77, 'y2': 535}, {'x1': 181, 'y1': 524, 'x2': 208, 'y2': 598}, {'x1': 160, 'y1': 293, 'x2': 192, 'y2': 315}, {'x1': 539, 'y1': 183, 'x2': 585, 'y2': 269}, {'x1': 583, 'y1': 320, 'x2': 597, 'y2': 385}]))
print(number_of_collisions([{'x1': 576, 'y1': 364, 'x2': 632, 'y2': 393}, {'x1': 179, 'y1': 6, 'x2': 269, 'y2': 55}, {'x1': 181, 'y1': 180, 'x2': 277, 'y2': 230}, {'x1': 198, 'y1': 297, 'x2': 209, 'y2': 389}, {'x1': 355, 'y1': 316, 'x2': 410, 'y2': 352}, {'x1': 306, 'y1': 365, 'x2': 367, 'y2': 412}, {'x1': 285, 'y1': 557, 'x2': 350, 'y2': 640}, {'x1': 151, 'y1': 579, 'x2': 178, 'y2': 655}, {'x1': 0, 'y1': 555, 'x2': 56, 'y2': 609}, {'x1': 289, 'y1': 416, 'x2': 309, 'y2': 507}, {'x1': 582, 'y1': 459, 'x2': 644, 'y2': 469}, {'x1': 411, 'y1': 530, 'x2': 501, 'y2': 583}, {'x1': 274, 'y1': 453, 'x2': 335, 'y2': 507}, {'x1': 519, 'y1': 86, 'x2': 562, 'y2': 133}, {'x1': 237, 'y1': 132, 'x2': 305, 'y2': 205}, {'x1': 462, 'y1': 379, 'x2': 480, 'y2': 391}, {'x1': 73, 'y1': 363, 'x2': 113, 'y2': 428}, {'x1': 362, 'y1': 298, 'x2': 416, 'y2': 356}, {'x1': 304, 'y1': 557, 'x2': 365, 'y2': 607}, {'x1': 276, 'y1': 138, 'x2': 313, 'y2': 173}, {'x1': 136, 'y1': 600, 'x2': 191, 'y2': 615}, {'x1': 384, 'y1': 162, 'x2': 455, 'y2': 180}, {'x1': 550, 'y1': 510, 'x2': 586, 'y2': 545}, {'x1': 318, 'y1': 28, 'x2': 364, 'y2': 89}, {'x1': 530, 'y1': 489, 'x2': 626, 'y2': 580}, {'x1': 433, 'y1': 596, 'x2': 528, 'y2': 619}, {'x1': 554, 'y1': 531, 'x2': 601, 'y2': 582}, {'x1': 283, 'y1': 322, 'x2': 360, 'y2': 380}, {'x1': 174, 'y1': 330, 'x2': 266, 'y2': 372}, {'x1': 11, 'y1': 578, 'x2': 61, 'y2': 650}, {'x1': 8, 'y1': 262, 'x2': 45, 'y2': 282}, {'x1': 175, 'y1': 100, 'x2': 238, 'y2': 184}, {'x1': 558, 'y1': 195, 'x2': 601, 'y2': 260}, {'x1': 333, 'y1': 80, 'x2': 354, 'y2': 115}, {'x1': 477, 'y1': 257, 'x2': 495, 'y2': 341}, {'x1': 280, 'y1': 311, 'x2': 299, 'y2': 339}, {'x1': 183, 'y1': 351, 'x2': 203, 'y2': 429}, {'x1': 219, 'y1': 571, 'x2': 239, 'y2': 609}, {'x1': 582, 'y1': 259, 'x2': 661, 'y2': 277}, {'x1': 77, 'y1': 457, 'x2': 116, 'y2': 484}, {'x1': 128, 'y1': 137, 'x2': 214, 'y2': 193}, {'x1': 597, 'y1': 153, 'x2': 607, 'y2': 169}, {'x1': 152, 'y1': 441, 'x2': 191, 'y2': 517}, {'x1': 132, 'y1': 531, 'x2': 183, 'y2': 561}, {'x1': 218, 'y1': 15, 'x2': 260, 'y2': 92}, {'x1': 316, 'y1': 286, 'x2': 396, 'y2': 324}, {'x1': 474, 'y1': 124, 'x2': 551, 'y2': 168}, {'x1': 178, 'y1': 68, 'x2': 192, 'y2': 162}, {'x1': 233, 'y1': 244, 'x2': 246, 'y2': 274}, {'x1': 224, 'y1': 21, 'x2': 259, 'y2': 77}, {'x1': 456, 'y1': 284, 'x2': 546, 'y2': 302}, {'x1': 174, 'y1': 108, 'x2': 218, 'y2': 206}, {'x1': 560, 'y1': 526, 'x2': 591, 'y2': 554}, {'x1': 294, 'y1': 209, 'x2': 383, 'y2': 249}, {'x1': 491, 'y1': 380, 'x2': 543, 'y2': 446}, {'x1': 15, 'y1': 108, 'x2': 79, 'y2': 168}, {'x1': 149, 'y1': 476, 'x2': 186, 'y2': 548}, {'x1': 591, 'y1': 195, 'x2': 658, 'y2': 285}, {'x1': 252, 'y1': 427, 'x2': 331, 'y2': 450}, {'x1': 180, 'y1': 162, 'x2': 244, 'y2': 234}, {'x1': 548, 'y1': 363, 'x2': 640, 'y2': 410}, {'x1': 359, 'y1': 220, 'x2': 429, 'y2': 272}, {'x1': 505, 'y1': 521, 'x2': 598, 'y2': 533}, {'x1': 95, 'y1': 209, 'x2': 150, 'y2': 260}, {'x1': 108, 'y1': 242, 'x2': 183, 'y2': 320}, {'x1': 565, 'y1': 350, 'x2': 660, 'y2': 438}, {'x1': 500, 'y1': 256, 'x2': 527, 'y2': 288}, {'x1': 214, 'y1': 596, 'x2': 297, 'y2': 636}, {'x1': 408, 'y1': 263, 'x2': 463, 'y2': 305}, {'x1': 484, 'y1': 205, 'x2': 569, 'y2': 217}, {'x1': 586, 'y1': 593, 'x2': 599, 'y2': 603}, {'x1': 8, 'y1': 526, 'x2': 97, 'y2': 585}, {'x1': 104, 'y1': 292, 'x2': 185, 'y2': 333}, {'x1': 368, 'y1': 69, 'x2': 464, 'y2': 103}, {'x1': 114, 'y1': 127, 'x2': 177, 'y2': 226}, {'x1': 254, 'y1': 282, 'x2': 312, 'y2': 362}, {'x1': 177, 'y1': 572, 'x2': 239, 'y2': 640}, {'x1': 113, 'y1': 325, 'x2': 173, 'y2': 381}, {'x1': 566, 'y1': 581, 'x2': 639, 'y2': 652}, {'x1': 266, 'y1': 158, 'x2': 358, 'y2': 187}, {'x1': 258, 'y1': 322, 'x2': 291, 'y2': 419}, {'x1': 308, 'y1': 115, 'x2': 373, 'y2': 151}, {'x1': 389, 'y1': 542, 'x2': 402, 'y2': 583}, {'x1': 289, 'y1': 112, 'x2': 376, 'y2': 197}, {'x1': 375, 'y1': 574, 'x2': 402, 'y2': 665}, {'x1': 95, 'y1': 344, 'x2': 110, 'y2': 398}, {'x1': 141, 'y1': 268, 'x2': 168, 'y2': 326}, {'x1': 75, 'y1': 154, 'x2': 127, 'y2': 229}, {'x1': 303, 'y1': 461, 'x2': 325, 'y2': 547}, {'x1': 549, 'y1': 319, 'x2': 644, 'y2': 329}, {'x1': 422, 'y1': 216, 'x2': 442, 'y2': 299}, {'x1': 2, 'y1': 553, 'x2': 91, 'y2': 631}, {'x1': 304, 'y1': 29, 'x2': 377, 'y2': 56}, {'x1': 558, 'y1': 416, 'x2': 568, 'y2': 499}, {'x1': 572, 'y1': 421, 'x2': 662, 'y2': 451}, {'x1': 527, 'y1': 462, 'x2': 545, 'y2': 524}, {'x1': 197, 'y1': 578, 'x2': 248, 'y2': 593}, {'x1': 77, 'y1': 457, 'x2': 105, 'y2': 516}, {'x1': 127, 'y1': 85, 'x2': 226, 'y2': 138}, {'x1': 362, 'y1': 278, 'x2': 377, 'y2': 291}]))
print(number_of_collisions([{'x1': 82, 'y1': 42, 'x2': 101, 'y2': 93}, {'x1': 446, 'y1': 436, 'x2': 504, 'y2': 474}, {'x1': 250, 'y1': 579, 'x2': 302, 'y2': 664}, {'x1': 248, 'y1': 299, 'x2': 309, 'y2': 313}, {'x1': 95, 'y1': 453, 'x2': 187, 'y2': 540}, {'x1': 241, 'y1': 72, 'x2': 276, 'y2': 154}, {'x1': 44, 'y1': 299, 'x2': 133, 'y2': 363}, {'x1': 253, 'y1': 595, 'x2': 326, 'y2': 650}, {'x1': 254, 'y1': 313, 'x2': 338, 'y2': 389}, {'x1': 557, 'y1': 248, 'x2': 567, 'y2': 338}, {'x1': 277, 'y1': 164, 'x2': 370, 'y2': 188}, {'x1': 203, 'y1': 410, 'x2': 260, 'y2': 437}, {'x1': 552, 'y1': 598, 'x2': 573, 'y2': 609}, {'x1': 507, 'y1': 131, 'x2': 524, 'y2': 171}, {'x1': 517, 'y1': 288, 'x2': 543, 'y2': 363}, {'x1': 394, 'y1': 528, 'x2': 433, 'y2': 615}, {'x1': 575, 'y1': 179, 'x2': 656, 'y2': 231}, {'x1': 385, 'y1': 195, 'x2': 405, 'y2': 226}, {'x1': 172, 'y1': 337, 'x2': 240, 'y2': 349}, {'x1': 254, 'y1': 226, 'x2': 269, 'y2': 260}, {'x1': 134, 'y1': 341, 'x2': 230, 'y2': 369}, {'x1': 439, 'y1': 30, 'x2': 489, 'y2': 76}, {'x1': 175, 'y1': 574, 'x2': 266, 'y2': 665}, {'x1': 339, 'y1': 341, 'x2': 404, 'y2': 392}, {'x1': 64, 'y1': 468, 'x2': 127, 'y2': 520}, {'x1': 339, 'y1': 529, 'x2': 383, 'y2': 627}, {'x1': 361, 'y1': 181, 'x2': 425, 'y2': 269}, {'x1': 96, 'y1': 464, 'x2': 184, 'y2': 485}, {'x1': 213, 'y1': 62, 'x2': 265, 'y2': 148}, {'x1': 90, 'y1': 202, 'x2': 114, 'y2': 264}, {'x1': 151, 'y1': 109, 'x2': 242, 'y2': 155}, {'x1': 517, 'y1': 534, 'x2': 556, 'y2': 617}, {'x1': 416, 'y1': 9, 'x2': 461, 'y2': 92}, {'x1': 113, 'y1': 169, 'x2': 174, 'y2': 191}, {'x1': 403, 'y1': 557, 'x2': 415, 'y2': 584}, {'x1': 21, 'y1': 173, 'x2': 83, 'y2': 239}, {'x1': 416, 'y1': 50, 'x2': 507, 'y2': 110}, {'x1': 290, 'y1': 517, 'x2': 303, 'y2': 607}, {'x1': 50, 'y1': 330, 'x2': 65, 'y2': 345}, {'x1': 192, 'y1': 516, 'x2': 221, 'y2': 547}, {'x1': 530, 'y1': 65, 'x2': 600, 'y2': 105}, {'x1': 316, 'y1': 147, 'x2': 375, 'y2': 177}, {'x1': 168, 'y1': 147, 'x2': 257, 'y2': 173}, {'x1': 316, 'y1': 451, 'x2': 343, 'y2': 506}, {'x1': 8, 'y1': 301, 'x2': 106, 'y2': 398}, {'x1': 46, 'y1': 354, 'x2': 95, 'y2': 383}, {'x1': 26, 'y1': 44, 'x2': 95, 'y2': 93}, {'x1': 196, 'y1': 541, 'x2': 293, 'y2': 580}, {'x1': 294, 'y1': 220, 'x2': 343, 'y2': 253}, {'x1': 339, 'y1': 556, 'x2': 387, 'y2': 579}, {'x1': 429, 'y1': 420, 'x2': 502, 'y2': 513}, {'x1': 397, 'y1': 590, 'x2': 425, 'y2': 681}, {'x1': 445, 'y1': 180, 'x2': 536, 'y2': 272}, {'x1': 461, 'y1': 324, 'x2': 494, 'y2': 399}, {'x1': 229, 'y1': 357, 'x2': 318, 'y2': 447}, {'x1': 546, 'y1': 146, 'x2': 603, 'y2': 172}, {'x1': 70, 'y1': 476, 'x2': 99, 'y2': 528}, {'x1': 432, 'y1': 53, 'x2': 458, 'y2': 149}, {'x1': 170, 'y1': 105, 'x2': 217, 'y2': 172}, {'x1': 127, 'y1': 446, 'x2': 211, 'y2': 528}, {'x1': 328, 'y1': 238, 'x2': 403, 'y2': 282}, {'x1': 187, 'y1': 467, 'x2': 228, 'y2': 511}, {'x1': 342, 'y1': 181, 'x2': 406, 'y2': 278}, {'x1': 378, 'y1': 237, 'x2': 462, 'y2': 282}, {'x1': 388, 'y1': 409, 'x2': 469, 'y2': 441}, {'x1': 241, 'y1': 398, 'x2': 258, 'y2': 456}, {'x1': 539, 'y1': 55, 'x2': 599, 'y2': 82}, {'x1': 3, 'y1': 514, 'x2': 62, 'y2': 597}, {'x1': 421, 'y1': 222, 'x2': 432, 'y2': 277}, {'x1': 399, 'y1': 169, 'x2': 409, 'y2': 259}, {'x1': 294, 'y1': 552, 'x2': 339, 'y2': 629}, {'x1': 457, 'y1': 32, 'x2': 537, 'y2': 82}, {'x1': 348, 'y1': 443, 'x2': 366, 'y2': 523}, {'x1': 133, 'y1': 278, 'x2': 195, 'y2': 349}, {'x1': 378, 'y1': 176, 'x2': 475, 'y2': 225}, {'x1': 365, 'y1': 153, 'x2': 380, 'y2': 222}, {'x1': 426, 'y1': 154, 'x2': 484, 'y2': 170}, {'x1': 492, 'y1': 453, 'x2': 592, 'y2': 523}, {'x1': 442, 'y1': 205, 'x2': 520, 'y2': 270}, {'x1': 447, 'y1': 90, 'x2': 511, 'y2': 152}, {'x1': 388, 'y1': 600, 'x2': 405, 'y2': 623}, {'x1': 297, 'y1': 201, 'x2': 355, 'y2': 282}, {'x1': 535, 'y1': 295, 'x2': 611, 'y2': 353}, {'x1': 325, 'y1': 93, 'x2': 369, 'y2': 170}, {'x1': 84, 'y1': 140, 'x2': 128, 'y2': 194}, {'x1': 2, 'y1': 366, 'x2': 30, 'y2': 446}, {'x1': 315, 'y1': 451, 'x2': 383, 'y2': 525}, {'x1': 163, 'y1': 425, 'x2': 257, 'y2': 513}, {'x1': 3, 'y1': 341, 'x2': 77, 'y2': 425}, {'x1': 55, 'y1': 589, 'x2': 77, 'y2': 684}, {'x1': 196, 'y1': 513, 'x2': 238, 'y2': 533}, {'x1': 333, 'y1': 568, 'x2': 359, 'y2': 630}, {'x1': 111, 'y1': 447, 'x2': 137, 'y2': 485}, {'x1': 68, 'y1': 600, 'x2': 96, 'y2': 694}, {'x1': 368, 'y1': 551, 'x2': 440, 'y2': 647}, {'x1': 409, 'y1': 451, 'x2': 486, 'y2': 518}, {'x1': 172, 'y1': 375, 'x2': 195, 'y2': 386}, {'x1': 459, 'y1': 566, 'x2': 481, 'y2': 642}, {'x1': 17, 'y1': 142, 'x2': 35, 'y2': 228}, {'x1': 183, 'y1': 194, 'x2': 245, 'y2': 208}]))
print(number_of_collisions([{'x1': 499, 'y1': 72, 'x2': 576, 'y2': 166}, {'x1': 535, 'y1': 537, 'x2': 632, 'y2': 584}, {'x1': 51, 'y1': 95, 'x2': 84, 'y2': 154}, {'x1': 428, 'y1': 150, 'x2': 444, 'y2': 162}, {'x1': 514, 'y1': 426, 'x2': 540, 'y2': 494}, {'x1': 316, 'y1': 287, 'x2': 379, 'y2': 304}, {'x1': 351, 'y1': 414, 'x2': 429, 'y2': 434}, {'x1': 278, 'y1': 247, 'x2': 378, 'y2': 273}, {'x1': 111, 'y1': 326, 'x2': 195, 'y2': 404}, {'x1': 496, 'y1': 434, 'x2': 516, 'y2': 521}, {'x1': 335, 'y1': 50, 'x2': 399, 'y2': 96}, {'x1': 47, 'y1': 48, 'x2': 65, 'y2': 96}, {'x1': 507, 'y1': 589, 'x2': 583, 'y2': 672}, {'x1': 469, 'y1': 467, 'x2': 530, 'y2': 527}, {'x1': 121, 'y1': 335, 'x2': 167, 'y2': 352}, {'x1': 194, 'y1': 277, 'x2': 244, 'y2': 290}, {'x1': 451, 'y1': 498, 'x2': 547, 'y2': 521}, {'x1': 271, 'y1': 542, 'x2': 315, 'y2': 636}, {'x1': 167, 'y1': 103, 'x2': 177, 'y2': 129}, {'x1': 76, 'y1': 220, 'x2': 162, 'y2': 247}, {'x1': 286, 'y1': 32, 'x2': 307, 'y2': 95}, {'x1': 574, 'y1': 248, 'x2': 606, 'y2': 322}, {'x1': 274, 'y1': 520, 'x2': 323, 'y2': 534}, {'x1': 396, 'y1': 261, 'x2': 467, 'y2': 335}, {'x1': 273, 'y1': 2, 'x2': 350, 'y2': 33}, {'x1': 170, 'y1': 446, 'x2': 256, 'y2': 487}, {'x1': 174, 'y1': 138, 'x2': 211, 'y2': 222}, {'x1': 413, 'y1': 103, 'x2': 471, 'y2': 115}, {'x1': 514, 'y1': 368, 'x2': 567, 'y2': 459}, {'x1': 521, 'y1': 469, 'x2': 559, 'y2': 563}, {'x1': 426, 'y1': 185, 'x2': 507, 'y2': 253}, {'x1': 371, 'y1': 487, 'x2': 423, 'y2': 541}, {'x1': 443, 'y1': 211, 'x2': 461, 'y2': 225}, {'x1': 553, 'y1': 397, 'x2': 625, 'y2': 487}, {'x1': 118, 'y1': 318, 'x2': 179, 'y2': 366}, {'x1': 418, 'y1': 98, 'x2': 503, 'y2': 176}, {'x1': 356, 'y1': 504, 'x2': 439, 'y2': 563}, {'x1': 126, 'y1': 97, 'x2': 169, 'y2': 141}, {'x1': 206, 'y1': 267, 'x2': 304, 'y2': 336}, {'x1': 45, 'y1': 288, 'x2': 123, 'y2': 317}, {'x1': 286, 'y1': 228, 'x2': 359, 'y2': 275}, {'x1': 34, 'y1': 155, 'x2': 73, 'y2': 193}, {'x1': 556, 'y1': 195, 'x2': 634, 'y2': 240}, {'x1': 297, 'y1': 142, 'x2': 336, 'y2': 188}, {'x1': 187, 'y1': 37, 'x2': 233, 'y2': 52}, {'x1': 587, 'y1': 21, 'x2': 659, 'y2': 83}, {'x1': 84, 'y1': 556, 'x2': 131, 'y2': 606}, {'x1': 172, 'y1': 561, 'x2': 261, 'y2': 583}, {'x1': 585, 'y1': 184, 'x2': 681, 'y2': 237}, {'x1': 361, 'y1': 486, 'x2': 383, 'y2': 581}, {'x1': 176, 'y1': 167, 'x2': 261, 'y2': 231}, {'x1': 82, 'y1': 28, 'x2': 117, 'y2': 67}, {'x1': 151, 'y1': 184, 'x2': 223, 'y2': 207}, {'x1': 320, 'y1': 210, 'x2': 368, 'y2': 299}, {'x1': 356, 'y1': 396, 'x2': 384, 'y2': 454}, {'x1': 235, 'y1': 575, 'x2': 309, 'y2': 641}, {'x1': 215, 'y1': 55, 'x2': 235, 'y2': 142}, {'x1': 381, 'y1': 491, 'x2': 463, 'y2': 546}, {'x1': 544, 'y1': 435, 'x2': 564, 'y2': 454}, {'x1': 576, 'y1': 62, 'x2': 665, 'y2': 83}, {'x1': 73, 'y1': 176, 'x2': 173, 'y2': 204}, {'x1': 168, 'y1': 599, 'x2': 214, 'y2': 622}, {'x1': 384, 'y1': 28, 'x2': 459, 'y2': 117}, {'x1': 543, 'y1': 142, 'x2': 600, 'y2': 240}, {'x1': 310, 'y1': 576, 'x2': 407, 'y2': 661}, {'x1': 273, 'y1': 456, 'x2': 348, 'y2': 504}, {'x1': 245, 'y1': 464, 'x2': 327, 'y2': 485}, {'x1': 560, 'y1': 184, 'x2': 654, 'y2': 260}, {'x1': 572, 'y1': 178, 'x2': 654, 'y2': 270}, {'x1': 32, 'y1': 14, 'x2': 94, 'y2': 90}, {'x1': 43, 'y1': 16, 'x2': 143, 'y2': 91}, {'x1': 121, 'y1': 271, 'x2': 155, 'y2': 282}, {'x1': 401, 'y1': 53, 'x2': 422, 'y2': 121}, {'x1': 305, 'y1': 363, 'x2': 342, 'y2': 385}, {'x1': 12, 'y1': 474, 'x2': 24, 'y2': 570}, {'x1': 193, 'y1': 454, 'x2': 216, 'y2': 471}, {'x1': 81, 'y1': 502, 'x2': 108, 'y2': 557}, {'x1': 316, 'y1': 164, 'x2': 371, 'y2': 238}, {'x1': 43, 'y1': 15, 'x2': 63, 'y2': 76}, {'x1': 14, 'y1': 301, 'x2': 79, 'y2': 357}, {'x1': 397, 'y1': 586, 'x2': 422, 'y2': 623}, {'x1': 310, 'y1': 313, 'x2': 398, 'y2': 342}, {'x1': 415, 'y1': 283, 'x2': 446, 'y2': 363}, {'x1': 375, 'y1': 46, 'x2': 393, 'y2': 146}, {'x1': 27, 'y1': 106, 'x2': 41, 'y2': 117}, {'x1': 220, 'y1': 91, 'x2': 308, 'y2': 160}, {'x1': 516, 'y1': 225, 'x2': 551, 'y2': 284}, {'x1': 153, 'y1': 191, 'x2': 214, 'y2': 289}, {'x1': 213, 'y1': 491, 'x2': 309, 'y2': 543}, {'x1': 368, 'y1': 183, 'x2': 434, 'y2': 199}, {'x1': 355, 'y1': 170, 'x2': 394, 'y2': 195}, {'x1': 129, 'y1': 522, 'x2': 172, 'y2': 547}, {'x1': 52, 'y1': 290, 'x2': 138, 'y2': 355}, {'x1': 491, 'y1': 319, 'x2': 562, 'y2': 369}, {'x1': 462, 'y1': 434, 'x2': 511, 'y2': 507}, {'x1': 486, 'y1': 308, 'x2': 499, 'y2': 345}, {'x1': 416, 'y1': 271, 'x2': 442, 'y2': 287}, {'x1': 538, 'y1': 587, 'x2': 636, 'y2': 606}, {'x1': 195, 'y1': 50, 'x2': 289, 'y2': 114}, {'x1': 21, 'y1': 281, 'x2': 33, 'y2': 370}]))
