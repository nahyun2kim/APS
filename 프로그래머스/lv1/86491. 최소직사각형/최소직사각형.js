function solution(sizes) {
    var a = 0
    var b = 0
    for(let i=0; i<sizes.length; i++){
        if(sizes[i][0] > sizes[i][1]){
            a = Math.max(a, sizes[i][0])
            b = Math.max(b, sizes[i][1])
        }else {
            a = Math.max(a, sizes[i][1])
            b = Math.max(b, sizes[i][0])
        }
    }
    return a * b
}