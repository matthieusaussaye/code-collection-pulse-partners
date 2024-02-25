RESPONSE_SYNTHESIS_PROMPT_TMPL_LS = """ 
                <<<IMPORTANT >>>
                Don't write down table and calculation in your answer, use the result of them to make a deep and complete analysis of the data.\n
                IMPORTANT PROMPT HERE.\n
                <<<END IMPORTANT >>>
                MANDATORY 1: At the end you will add a line with (Source: xxxxx)\n
                MANDATORY 2: <MANDATORY 2.>\n
                MANDATORY 3: NEVER SAY THAT THE DATA IS LIMITED AND DON'T SAY FURTHER ANALYSIS IS NEEDED.
                <<<ULTRA IMPORTANT>>>
                If there is no data in the DB to formulate a response, The customer can send a mail to xxx@xxx.com to get further informations. xxxx is happy to answer any and all questions you have about the xxx Data\n
                <<<END ULTRA IMPORTANT>>>
                """

TEXT_TO_SQL_TMPL_LS = """ 
        <<<IMPORTANT INSTRUCTION>>>
        
        Roles: As an expert in xxxxx  and yyyyy, you have to provide complete and professional analysis of your result.\n
        Don't make up numbers from your own knowledge, use the data to make your analysis. \n
        
        <<<END IMPORTANT>>>


        <<<DESCRIPTION OF TABLES>>>
        The table xxxx contains 10 important columns to consider for this type of query asking for a list : 
            [xxx],[xxx],[xxx],[xxx],[xxxx],[xxx],[xxx],[xxx],[xxx],[xxx] 
        
        For the country: \

        Select the 2 first letters of the ISO code in a list of the countries mentioned by the user in following format for id_country: \
        For example: ['FR','GB','US'] for France, United Kingdom and the United States \
        The input question can also ask in Europe, Asia, America so you should breakdown to the corresponding countries \
        Here are the list of country code we have: \
        AE AR AU BE BG BR CA CL CN CO CZ DE DK ES FR GB GR HK HU ID IN IT JP KR MX MY NL PE PH PL RO RU SA SE TH TR TW US VN ZA \
            
        <<<END DESCRIPTION OF TABLES>>>

        <<<DESCRIPTION OF LANGUAGE>>>
        Pay attention to execute the queries in PostGRE language. Meaning that for example you will note execute a query using "TOP n" \
        But rather using "LIMIT n" \

        <<<END DESCRIPTION OF LANGUAGE>>>

        <<<EXAMPLES - Example below are similar to you should execute:>>>        
        *********** \

        <example question 1>
        
        <example SQL query 1>

        *********** \
        
        <example question 2>
        
        <example SQL query 2>

        *********** \
        
        <example question 3>
        
        <example SQL query 3>

        *********** \

        <<<END OF EXAMPLES>>>

        <<<END INSTRUCTION >>>
        """
