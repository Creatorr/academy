################################################################################
#
#  The function alphabetize the list based on the n-th letter of each word.
#  Parameters:
#    list_:  a string (containing a list of words)
#    n:      an integer (n)
#
################################################################################

def sort_it(list_,n):
    list_for_sorted = [word.strip() for word in list_.split(",")]
    sorted_list = sorted(list_for_sorted,
                         key=lambda list_for_sorted: list_for_sorted[n - 1])
    return ", ".join(sorted_list)

#print sort_it("Ulrich Kesler, August Samuel Wahlen, Arthur von Streit, Helmut Rennenkampf, Anton Ferner, Fritz Josef Bittenfeld, Hildegard von Mariendorf, Cornelius Lutz, Siegfried Kircheis, Wolfgang Mittermeyer, Emil von Secla, Paul von Oberstein, Karl Robert Steinmetz, Reinhard von Lohengramm, Adalbert von Fahrenheit, Theodor von Lucke, Neidhardt Muller, Karl Gustav Kempf, Oskar von Reuenthal, Ernst von Eisenach", 7)
