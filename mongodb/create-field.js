db.words.update({}, {$set : {"submit":0}}, {upsert:false, multi:true})
// 현재 DB의 words 컬렉션에서 submit이라는 새로운 필드를 생성하고 0으로 초기화한다.
