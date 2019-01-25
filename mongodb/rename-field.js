db.words.update({}, {$rename:{"user_id":"userId"}}, false, true);
// 현재 DB의 words 컬렉션에서 user_id 필드의 이름을 userId로 변경한다.
