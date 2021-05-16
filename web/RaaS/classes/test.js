const c = require("crypto");
const hasher = c.createHash("sha256");
const hash = hasher.update(
    (+"9875910160063706" + +"8797123715865698").toString() + "8797123715865698".toString() + "0" +
    "9999999" + "7h15_15_7h3_50l71357_50l7_y0u_h4v3_3v3r_533n!" + "EUR"
).digest("hex");
console.log(hash)