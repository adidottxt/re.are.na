import React from "react"
import ApolloClient from 'apollo-boost'
import { ApolloProvider } from 'react-apollo'

import Header from "./Header"
import Button from "./Button"
import HeaderInfo from "./HeaderInfo"
import RowList from "./RowList"

import "../css/App.css"

// Apollo Client setup
const client = new ApolloClient({
  uri: 'http://127.0.0.1:5000/graphql'
})


function App() {
    return (
        <ApolloProvider client={client}>
            <div>
                <Header />
                <HeaderInfo />
                <RowList />
                <Button text='Refresh' />
            </div>
        </ApolloProvider>
    )
}

export default App
