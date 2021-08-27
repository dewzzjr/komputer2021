console.log("test");

// variable
var nama = "Dewangga";
var umur = 25;
var lakiLaki = true;

if (!lakiLaki) {
    console.log("saya perempuan"); 
} else {
    console.log("saya laki laki"); 
}

var daftarNama = [
    "Dewangga",
    "Prasetya",
    "Praja",
]

var panjang = daftarNama.length
daftarNama.push("Tambahan")

console.log(daftarNama[3])

// 1. loop variable
// 2. end value
// 3. loop operation
for (var i = 0; i < 5; i++) {
    console.log(i + " loop");
}

var i = 0;
while (i < 5) {
    console.log(i + " loop2");
    i++
}