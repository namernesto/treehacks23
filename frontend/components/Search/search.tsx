import React, { useEffect, useState } from "react";
import { InputGroup, InputLeftElement, Input, Box, ButtonGroup, Button } from '@chakra-ui/react';



// interface Props {
//   articles: [IArticle];
//   setArticlesList: React.Dispatch<(prevState: IArticle[]) => IArticle[]>;
//   currentTab: string;
//   setTab: React.Dispatch<(prevState: string) => string>;
// }

export default function SearchBar(test:any) {
    
    return (
        <div>
            <Box
                display='flex'
                flexDir='column'
                alignItems='center'
                justifyContent='center'
                width='100%'
                py={12}
                bgPosition='center'
                bgRepeat='no-repeat'
                
                mb={4}
            >
                <Input placeholder="What do you want to explore?"  width='auto' size='lg' mb={5}/>

                <Button colorScheme='red'>Search!</Button>

            </Box>

        </div>
    );
}

