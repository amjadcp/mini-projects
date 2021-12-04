const Web3 = require('web3');
let web3 = new Web3('https://rinkeby.infura.io/v3/f13e01f6d1d24c3f86660ec1dbd6fb36');
const abi = [{"inputs":[],"name":"Greeter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}];
const address = "0x2524d963D19899D50300569D885BE1f5aEF368ff";
let contract = new web3.eth.Contract(abi, address);
contract.methods.greet().call( (err, result)=>{
    console.log(result);
});
