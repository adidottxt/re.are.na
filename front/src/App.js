import React from "react"

import Header from "./Header"
import Block from "./Block"
import Info from "./Info"

function App() {
    return (
        <div>
            <Header />
            <Block src='https://d2w9rnfcy7mm78.cloudfront.net/4039714/original_0e0254a0a1e901e4f67aacbebd6812e6.jpg?1554784576'/>
            <Info />
            <Block src='https://d2w9rnfcy7mm78.cloudfront.net/1580881/original_eae97b74b09c9707caf977f53fe38b57.png?1515539345'/>
            <Info />
            <Block src='https://d2w9rnfcy7mm78.cloudfront.net/2619145/original_d1009818b14274917d27b5a1a1757931.jpg?1535552897'/>
            <Info />
        </div>
    )
}

export default App
