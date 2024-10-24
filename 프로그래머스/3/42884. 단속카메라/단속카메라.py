def solution(routes):
    # 1. 차량 오름차순 정렬
    routes.sort(key = lambda x : (x[0], x[1]), reverse=True)
    
    # 2. 차량의 진출 지점에 카메라를 임시 설치하고 겹칠 수 있는 부분까지 pass
    cnt = 0
    camera = -30001
    while routes:
        st, ed = routes.pop()
        if st > camera:
            cnt += 1
            camera = ed
        else:
            camera = min(camera, ed)
    
    return cnt