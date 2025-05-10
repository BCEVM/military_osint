def run():
    print("\n=== Satellite Viewer ===")
    lat = input("Latitude >> ")
    lon = input("Longitude >> ")
    print("[+] Buka Sentinel Hub EO Browser:")
    print(f"https://apps.sentinel-hub.com/eo-browser/?lat={lat}&lng={lon}&zoom=12")
