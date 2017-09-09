import fresh_tomatoes
import media

''' Script to produce movie website.  '''


vivegam = media.Movie("VIVEGAM",
                      " ",
                      "https://goo.gl/vjxEyL",
                      "https://youtu.be/uM7zTAMFRxc")

bahubali = media.Movie("BAHUBALI 2",
                       " ",
                       "https://goo.gl/XiDZW1",
                       "https://youtu.be/94BzBOpv42g")

singam3 = media.Movie("S 3",
                      " ",
                      "https://goo.gl/VdArbn",
                      "https://youtu.be/CP9DinMVFq8")

bairavaa = media.Movie("BAIRAVAA",
                       " ",
                       "https://goo.gl/mRNC6n",
                       "https://youtu.be/bhTN4PDm6fc")

yeman = media.Movie("YEMAN",
                    " ",
                    "https://goo.gl/whXtJ6",
                    "https://youtu.be/F01dWVxih_A")

motta = media.Movie("MOTTA SIVA KETTA SIVA",
                    " ",
                    "https://goo.gl/vYaQbP",
                    "https://youtu.be/pDOZvta5uio")

movies = [vivegam, bahubali, singam3, bairavaa, yeman, motta]
fresh_tomatoes.open_movies_page(movies)
