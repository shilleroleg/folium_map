import simplekml
import first_map as fm

brand, longitude, latitude, address, diesel = fm.read_gas_list("gas list.xls")

kml_sibir = simplekml.Kml()

for i in range(len(longitude)):
    if longitude[i] >= 54:
        pnt = kml_sibir.newpoint(name=brand[i], description=address[i],
                                 coords=[(longitude[i], latitude[i])])   # lon, lat, optional height
else:
    kml_sibir.save("gas_map_sibir.kml")

kml_eur = simplekml.Kml()

for i in range(len(longitude)):
    if longitude[i] < 54:
        pnt = kml_eur.newpoint(name=brand[i], description=address[i],
                               coords=[(longitude[i], latitude[i])])   # lon, lat, optional height
else:
    kml_eur.save("gas_map_eur.kml")
