import React from "react"

import Header from "./js/Header"
import Button from "./js/Button"
import HeaderInfo from "./js/HeaderInfo"
import Row from "./js/Row"

function App() {
    return (
        <div>
            <Header />
            <HeaderInfo />

            <Row
                src='https://d2w9rnfcy7mm78.cloudfront.net/4771939/original_1c3af1831f95e7d71d0674227c114072.jpg?1565150930'
                title='test-title'
                channel='test-chan'
                date='test-date'
            />
            <Row
                src='https://d2w9rnfcy7mm78.cloudfront.net/1580881/original_eae97b74b09c9707caf977f53fe38b57.png?1515539345'
                title='test-title'
                channel='test-chan'
                date='test-date'
            />
            <Row
                src='https://d2w9rnfcy7mm78.cloudfront.net/2619145/original_d1009818b14274917d27b5a1a1757931.jpg?1535552897'
                title='test-title'
                channel='test-chan'
                date='test-date'
            />
            <Button text='Refresh' />
        </div>
    )
}

export default App
