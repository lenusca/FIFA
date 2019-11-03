<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
    <xsl:template match="/Players">
        <html>
            <body>

                    <xsl:for-each select="Player">
                         <h1>
                             <xsl:value-of select="Player_Name"/>
                         </h1>
                        <!--
                        <h1>
                            <xsl:value-of select="overall"/>
                        </h1>
                        -->

                        <table border = "1">
                        <tr>
                            <th>NAME</th>
                            <th>RAT</th>
                            <th>POS</th>
                            <th>AGE</th>
                            <th>HEIGHT</th>
                            <th>WEIGHT</th>
                        </tr>
                        <xsl:for-each select="Players" >
                            <xsl:sort select="Overall" /> <!-- data-type="number" /> -->
                            <tr>
                                    <td>
                                        <xsl:value-of select="Photo"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="Player_Name"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="Overall"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="Position"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="Age"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="Height"/>
                                    </td>
                                    <td>
                                        <xsl:value-of select="Weight"/>
                                    </td>
                            </tr>
                         </xsl:for-each>
                           </table>
                    </xsl:for-each>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>