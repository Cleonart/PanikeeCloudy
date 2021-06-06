def model(name, number, lat, long, category):
    return {
    	"EmergencyFacilityName"     : name,
        "EmergencyFacilityNumber"   : number,
        "EmergencyFacilityLat"      : lat,
        "EmergencyFacilityLong"     : long,
        "EmergencyFacilityCategory" : category
    }
