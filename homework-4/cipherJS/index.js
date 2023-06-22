import { createCipheriv, createDecipheriv } from 'crypto'

const cipher = (createCipheriv(
    'aes-256-cbc',
    "thisisa_32_byte_long_key_I_think",
    "dog1234567890123"
))

console.log(cipher.update("ow are you today?", "utf8", "hex") + cipher.final("hex"))