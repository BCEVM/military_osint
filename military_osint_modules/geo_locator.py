def run():
    print("\n=== GeoLocator ===")
    lat = input("Latitude (contoh: 37.7749) >> ")
    lon = input("Longitude (contoh: -122.4194) >> ")
    print("\n[+] Google Maps:")
    print(f"https://www.google.com/maps?q={lat},{lon}")
    print("\n[+] SunCalc untuk waktu & arah bayangan:")
    print(f"https://suncalc.org/#{lat},{lon},12")
