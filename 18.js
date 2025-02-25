// 객체와 레퍼런스 카운트에 대한 예시

// players 객체 생성
let players = {
    boys : {
        Bergkamp : "Striker"
    }
}
// players 객체의 레퍼런스 카운트는 1입니다.

// persons 변수에 players 객체를 할당
let persons = players
// players 객체의 레퍼런스 카운트는 2가 됩니다.

// players 변수에 새로운 배열을 할당
players = ["Son", "Park"]
// 이전에 players 객체가 참조하고 있던 { boys: { Bergkamp: "Striker" } } 객체의 레퍼런스 카운트는 1이 됩니다.
// persons 변수가 여전히 { boys: { Bergkamp: "Striker" } } 객체를 참조하고 있기 때문입니다.

// human 변수에 persons 객체의 boys 속성을 할당
let human = persons.boys
// { boys: { Bergkamp: "Striker" } } 객체의 레퍼런스 카운트는 여전히 1입니다.

// persons 변수에 새로운 문자열을 할당
persons = "persons"
// 이전에 persons 변수가 참조하고 있던 { boys: { Bergkamp: "Striker" } } 객체의 레퍼런스 카운트는 0이 됩니다.
// { boys: { Bergkamp: "Striker" } } 객체를 참조하고 있던 변수가 더 이상 없기 때문입니다.

// { boys: { Bergkamp: "Striker" } } 객체는 가비지 컬렉션의 대상이 됩니다.
// 가비지 컬렉션은 메모리 관리를 위해 사용되는 프로세스로, 더 이상 참조되지 않는 객체를 메모리에서 제거하는 역할을 합니다.