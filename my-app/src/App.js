import React from "react"

import Header from "./js/Header"
import Button from "./js/Button"
import HeaderInfo from "./js/HeaderInfo"
import Row from "./js/Row"
import TextRow from "./js/TextRow"

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
                src='https://d2w9rnfcy7mm78.cloudfront.net/4633641/display_94c1620f3ef1f7d2dc7008d0849f39b8.png?1563197545'
                title='test-title'
                channel='test-chan'
                date='test-date'
            />
            <TextRow
                src='https://are.na/block/4184924'
                text='testingtttttttttttttttttttttttttttttttttttttttttestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttestingestingestingestingestingestingestingestingestingestingestingestingesttttttttttttttttttttttttttttttttttttttttttestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingestingesting'
                title=''
                channel='snippets'
                date='test-date'
            />
            <Button text='Refresh' />
        </div>
    )
}

export default App
