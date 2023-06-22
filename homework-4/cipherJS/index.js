import { createCipheriv, createDecipheriv } from 'crypto'

const args = process.argv.slice(2)

if (args.length != 4) {
    console.log("Please enter commands in the following structure: node index.js -e/-d string key iv")
    process.exit(1)
}

if (args[0] === "-e") {
    console.log("encrypting")
    console.log(encrypt(args[1], args[2], args[3]))
} else if (args[0] === "-d") {
    console.log("decrypting")
    console.log(decrypt(args[1], args[2], args[3]))
} else {
    console.log("Please provide a valid flag (-e or -d)")
    process.exit(1)
}


function encrypt(string, key, iv) {
    const cipher = (createCipheriv(
        'aes-256-cbc',
        key,
        iv
    ))
    return cipher.update(string, "utf8", "hex") + cipher.final("hex")
}

function decrypt(string, key, iv) {
    const decipher = createDecipheriv(
        'aes-256-cbc',
        key,
        iv
    )
    return decipher.update(string, "hex", "utf8") + decipher.final("utf8")
}
