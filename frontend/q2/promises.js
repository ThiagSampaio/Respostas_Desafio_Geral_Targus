const request = require('request-promise')

const pegarIP = async () => {
    const ip1 = await request("https://www.google.com.br")
    const ip2 = await request("https://stackoverflow.com/")
    const ip3 = await request("https://www.python.org")
    const ip4 = await request("https://www.javascript.com/")
    const ip5 = await request("https://golang.org/")
    console.log('OK')
}

pegarIP()