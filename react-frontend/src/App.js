import React from "react"
import ApolloClient from 'apollo-boost'
import { ApolloProvider } from 'react-apollo'

import Header from "./js/Header"
import Button from "./js/Button"
import HeaderInfo from "./js/HeaderInfo"
import RowList from "./js/RowList"

import "./css/App.css"

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
