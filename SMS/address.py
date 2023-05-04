from geopy.geocoders import Nominatim

def reverse_geocode(latitude, longitude):
    # Nominatim 객체 생성
    geolocator = Nominatim(user_agent="my-application-1")

    # 위도와 경도를 이용하여 주소 가져오기
    location = geolocator.reverse(str(latitude) + " " + str(longitude))

    # 주소 출력 (문자열 분리 후 뒤집기, 두 번째 값 삭제)
    address_list = location.address.split(', ')
    del address_list[-2:]
    reversed_address = ' '.join(address_list[::-1])
    
    return reversed_address

print(reverse_geocode(37.211745, 126.953032))