export interface Article {
  id: number
  title: string
  content: string
  published: boolean
}

export interface ArticleCollection {
  member: Article[]
  totalItems: number
}
