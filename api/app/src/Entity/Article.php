<?php

declare(strict_types=1);

namespace App\Entity;

use ApiPlatform\Metadata\{ApiResource, Get, GetCollection, Post, Patch, Delete};
use Doctrine\ORM\Mapping as ORM;
use Symfony\Component\Validator\Constraints as Assert;

#[ORM\Entity]
#[ApiResource(
    operations: [new Get(), new GetCollection(), new Post(), new Patch(), new Delete()],
    paginationItemsPerPage: 20,
    order: ['id' => 'DESC'],
)]
class Article
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(length: 160)]
    #[Assert\NotBlank(normalizer: 'trim')]
    #[Assert\Length(max: 160)]
    public string $title = '';

    #[ORM\Column(type: 'text')]
    public string $content = '';

    #[ORM\Column]
    public bool $published = false;

    public function getId(): ?int
    {
        return $this->id;
    }
}
